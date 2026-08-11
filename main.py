import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


class Painel(discord.ui.View):

    @discord.ui.select(
        placeholder="Clique para selecionar uma Opção",
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
            )
        ]
    )
    async def selecionar(
        self,
        interaction: discord.Interaction,
        select: discord.ui.Select
    ):
        escolha = select.values[0]

        if escolha == "informacoes":
            await interaction.response.send_message(
                "ℹ️ Aqui estão as informações do servidor.",
                ephemeral=True
            )

        elif escolha == "suporte":
            await interaction.response.send_message(
                "🎧 Entre em contato com a equipe.",
                ephemeral=True
            )


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.tree.command(
    name="painel",
    description="Envia o painel do servidor"
)
async def painel(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Painel Delrio",
        description="Selecione uma opção abaixo.",
        color=discord.Color.red()
    )

    await interaction.response.send_message(
        embed=embed,
        view=Painel()
    )


@bot.event
async def setup_hook():
    await bot.tree.sync()


bot.run(TOKEN)
