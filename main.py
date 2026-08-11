import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("A variável DISCORD_TOKEN não foi configurada na Railway.")


intents = discord.Intents.default()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


class Painel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        select = discord.ui.Select(
            placeholder="Clique para selecionar uma Opção",
            custom_id="painel_opcoes",
            options=[
                discord.SelectOption(
                    label="Informações",
                    description="Veja as informações do serviço",
                    emoji="ℹ️",
                    value="informacoes"
                ),
                discord.SelectOption(
                    label="Suporte",
                    description="Entre em contato com a equipe",
                    emoji="🎧",
                    value="suporte"
                ),
            ]
        )

        select.callback = self.selecionar
        self.add_item(select)

    async def selecionar(self, interaction: discord.Interaction):
        escolha = interaction.data["values"][0]

        if escolha == "informacoes":
            embed = discord.Embed(
                title="ℹ️ Informações",
                description=(
                    "Confira abaixo as informações da comunidade.\n\n"
                    "Caso tenha alguma dúvida, utilize a opção **Suporte**."
                ),
                color=discord.Color.blue()
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

        elif escolha == "suporte":
            embed = discord.Embed(
                title="🎧 Suporte",
                description=(
                    "Precisa de ajuda?\n\n"
                    "Entre em contato com a equipe através do canal de suporte."
                ),
                color=discord.Color.blue()
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )


class BotaoSuporte(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="🎮 Discord do Servidor",
            style=discord.ButtonStyle.secondary,
            custom_id="discord_servidor"
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "🎮 Entre no servidor através do convite disponibilizado pela equipe.",
            ephemeral=True
        )


class PainelCompleto(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        select = discord.ui.Select(
            placeholder="Clique para selecionar uma Opção",
            custom_id="painel_principal",
            options=[
                discord.SelectOption(
                    label="Informações",
                    description="Veja as informações do servidor",
                    emoji="ℹ️",
                    value="informacoes"
                ),
                discord.SelectOption(
                    label="Suporte",
                    description="Entre em contato com a equipe",
                    emoji="🎧",
                    value="suporte"
                ),
            ]
        )

        select.callback = self.selecionar
        self.add_item(select)

        self.add_item(BotaoSuporte())

    async def selecionar(self, interaction: discord.Interaction):
        escolha = interaction.data["values"][0]

        if escolha == "informacoes":
            embed = discord.Embed(
                title="ℹ️ Informações",
                description=(
                    "**Bem-vindo(a)!**\n\n"
                    "Aqui você encontra as principais informações "
                    "da comunidade e dos serviços disponíveis."
                ),
                color=discord.Color.blue()
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

        elif escolha == "suporte":
            embed = discord.Embed(
                title="🎧 Suporte",
                description=(
                    "Para receber atendimento, procure a equipe "
                    "responsável pelo suporte."
                ),
                color=discord.Color.blue()
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    try:
        synced = await tree.sync()
        print(f"{len(synced)} comando(s) sincronizado(s).")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")


@tree.command(
    name="painel",
    description="Envia o painel principal do servidor."
)
async def painel(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Bem-vindo(a) à Delrio | 1K",
        description=(
            "Este é seu servidor, novinho em folha.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 **Informações do Serviço**\n\n"
            "① Confira as informações abaixo\n"
            "② Utilize o menu para acessar as opções\n"
            "③ Em caso de dúvidas, procure o suporte\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔍 **Servidor:** Disponível no canal de informações\n"
            "🚚 **Porta:** Consulte a equipe responsável\n\n"
            "Selecione uma opção no menu abaixo."
        ),
        color=discord.Color.dark_theme()
    )

    embed.set_footer(
        text="Delrio • Sistema de Atendimento"
    )

    await interaction.response.send_message(
        embed=embed,
        view=PainelCompleto()
    )


bot.run(TOKEN)
