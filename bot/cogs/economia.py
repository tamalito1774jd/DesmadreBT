import discord
from discord.ext import commands, tasks
from bot.utils.database import db
from bot.utils.embeds import *
from bot.config import *
import random

class Economia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns_trabajo = {}
        self.cooldowns_robo = {}
    
    @commands.command()
    async def dinero(self, ctx, usuario: discord.User = None):
        """Ver dinero disponible"""
        usuario = usuario or ctx.author
        datos = db.get_user(usuario.id)
        
        if not datos:
            db.create_user(usuario.id, usuario.name)
            datos = db.get_user(usuario.id)
        
        embed = crear_embed_usuario(
            "💰 Tu Dinero",
            usuario,
            dinero=datos[2]
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def trabajo(self, ctx):
        """Trabajar para ganar dinero"""
        user_id = ctx.author.id
        
        # Verificar cooldown
        if user_id in self.cooldowns_trabajo:
            tiempo_restante = WORK_COOLDOWN - (datetime.now().timestamp() - self.cooldowns_trabajo[user_id])
            if tiempo_restante > 0:
                embed = crear_embed_error(
                    "Cooldown",
                    f"Debes esperar {int(tiempo_restante)} segundos para trabajar de nuevo"
                )
                return await ctx.send(embed=embed)
        
        # Crear usuario si no existe
        datos = db.get_user(user_id)
        if not datos:
            db.create_user(user_id, ctx.author.name)
        
        # Dar dinero
        cantidad = random.randint(WORK_MIN_AMOUNT, WORK_MAX_AMOUNT)
        db.add_dinero(user_id, cantidad)
        db.add_transaccion(None, user_id, cantidad, "trabajo")
        
        self.cooldowns_trabajo[user_id] = datetime.now().timestamp()
        
        embed = crear_embed_exito(
            "Trabajo Completado",
            f"Has ganado **${cantidad:,}** trabajando\nTe espera más trabajo en {WORK_COOLDOWN//60} minutos"
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def enviar(self, ctx, usuario: discord.User, cantidad: int):
        """Enviar dinero a otro usuario"""
        if cantidad <= 0:
            embed = crear_embed_error("Error", "La cantidad debe ser mayor a 0")
            return await ctx.send(embed=embed)
        
        # Verificar que tenga suficiente dinero
        datos_sender = db.get_user(ctx.author.id)
        if not datos_sender or datos_sender[2] < cantidad:
            embed = crear_embed_error("Dinero Insuficiente", "No tienes suficiente dinero")
            return await ctx.send(embed=embed)
        
        # Crear usuario receptor si no existe
        datos_receiver = db.get_user(usuario.id)
        if not datos_receiver:
            db.create_user(usuario.id, usuario.name)
        
        # Realizar transacción
        db.add_dinero(ctx.author.id, -cantidad)
        db.add_dinero(usuario.id, cantidad)
        db.add_transaccion(ctx.author.id, usuario.id, cantidad, "transferencia")
        
        embed = discord.Embed(
            title="💸 Transferencia Exitosa",
            description=f"{ctx.author.mention} envió **${cantidad:,}** a {usuario.mention}",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def robar(self, ctx, usuario: discord.User):
        """Intentar robar dinero a otro usuario"""
        user_id = ctx.author.id
        
        # Verificar cooldown
        if user_id in self.cooldowns_robo:
            tiempo_restante = ROB_COOLDOWN - (datetime.now().timestamp() - self.cooldowns_robo[user_id])
            if tiempo_restante > 0:
                embed = crear_embed_error(
                    "Cooldown",
                    f"Debes esperar {int(tiempo_restante)} segundos para robar de nuevo"
                )
                return await ctx.send(embed=embed)
        
        # Obtener datos de la víctima
        datos_victima = db.get_user(usuario.id)
        if not datos_victima or datos_victima[2] == 0:
            embed = crear_embed_error("Sin Dinero", f"{usuario.mention} no tiene dinero para robar")
            return await ctx.send(embed=embed)
        
        # 50% de probabilidad
        if random.random() > 0.5:
            cantidad = random.randint(ROB_MIN_AMOUNT, min(ROB_MAX_AMOUNT, datos_victima[2]))
            db.add_dinero(user_id, cantidad)
            db.add_dinero(usuario.id, -cantidad)
            db.add_transaccion(usuario.id, user_id, cantidad, "robo")
            
            embed = crear_embed_exito(
                "¡Robo Exitoso!",
                f"¡Le robaste **${cantidad:,}** a {usuario.mention}!"
            )
            self.cooldowns_robo[user_id] = datetime.now().timestamp()
            await ctx.send(embed=embed)
        else:
            embed = crear_embed_error(
                "¡Atrapado!",
                f"¡{usuario.mention} te atrapó intentando robar! Tu nombre está en la lista negra"
            )
            self.cooldowns_robo[user_id] = datetime.now().timestamp()
            await ctx.send(embed=embed)
    
    @commands.command()
    async def top_dinero(self, ctx):
        """Ver el top 10 usuarios por dinero"""
        usuarios = db.get_top_usuarios(10)
        if not usuarios:
            embed = crear_embed_error("Error", "No hay datos disponibles")
            return await ctx.send(embed=embed)
        
        embed = crear_embed_leaderboard("💰 Top 10 - Dinero", usuarios, tipo="dinero")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Economia(bot))
