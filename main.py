import discord
from discord import app_commands

id_do_servidor = 1014715343006089307 #Coloque aqui o ID do seu servidor

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'ponto', description='bater ponto') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"você Abriu um bate-ponto", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'fechar', description='Fecha Bp') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Você Fechou o seu Bate-ponto", ephemeral = False)
  
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'pausar', description='pausar') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Você pausou seu bate-ponto!", ephemeral = False)
  
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'voltar', description='Voltar da Pausa') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Você saiu da Pausa", ephemeral = False)
  
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'terminar', description='Terminar bp') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Você fechou o seu bate-ponto. Agora calcule o total de horas!", ephemeral = False)
  
aclient.run('MTAxNTQ0NTcxMzk1NTU4NjEzOA.Gr7Jxb.DJlj7iXcaTnY2usi3nWBAmnwbZxXx7S3_LwaVo')