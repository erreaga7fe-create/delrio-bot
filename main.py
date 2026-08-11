import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN não foi configurado na Railway.")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


# =========================
# MENU DE OPÇÕES
# =========================

class MenuOpcoes(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(
                label="Download Certificado Hs Pescoço",
                description="Baixe o certificado da proxy Hs Pescoço",
                emoji="🗄️",
                value="certificado"
            ),

            discord.SelectOption(
                label="Registre seu IP Free",
                description="1 Registro por conta",
                emoji="📡",
                value="registrar"
            )
        ]

        super().__init__(
            placeholder="Clique para selecionar uma Opção",
            options=options,
            custom_id="menu_opcoes_delrio"
        )

    async def callback(self, interaction: discord.Interaction):

        escolha = self.values[0]

        if escolha == "certificado":

            await interaction.response.send_message(
                "🗄️ **Download Certificado Hs Pescoço**\n\n"
                "Selecione esta opção para acessar as informações "
                "disponíveis sobre o certificado.",
                ephemeral=True
            )

        elif escolha == "registrar":

            await interaction.response.send_message(
                "📡 **Registre seu IP Free**\n\n"
                "Você possui **1 registro por conta**.",
                ephemeral=True
            )


# =========================
# PAINEL
# =========================

class PainelView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MenuOpcoes())


# =========================
# COMANDO !painel
# =========================

@bot.command()
@commands.has_permissions(administrator=True)
async def painel(ctx):

    embed = discord.Embed(
        title="Proxy iOS FREE",
        description=(
            "① Instale o certificado no seu dispositivo\n"
            "② Configure a proxy no seu Wi-Fi\n"
            "③ Abra o Free Fire e entre na sua conta\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "❔ proxy hs/antena\n"
            "🔎 Servidor: `93.127.132.29`\n"
            "🚚 Porta: `10047`"
        ),
        color=discord.Color.dark_grey()
    )

    await ctx.send(
        embed=embed,
        view=PainelView()
    )


# =========================
# BOT ONLINE
# =========================

@bot.event
async def on_ready():

    print(f"✅ Bot conectado como {bot.user}")
    print("✅ Painel carregado.")


bot.run(TOKEN)
