import discord
from discord import app_commands
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

worship_count = 0

class WorshipView(discord.ui.View):

    @discord.ui.button(label="👍 숭배하기", style=discord.ButtonStyle.success)
    async def worship_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        global worship_count
        worship_count += 1

        embed = interaction.message.embeds[0]
        embed.set_field_at(
            0,
            name="현재 숭배자 수",
            value=f"{worship_count}명",
            inline=False
        )

        await interaction.response.edit_message(embed=embed, view=self)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} 준비 완료!')


@bot.tree.command(name="기습숭배", description="이시진을 숭배합니다")
async def worship(interaction: discord.Interaction):

    global worship_count

    colors = [
        discord.Color.red(),
        discord.Color.blue(),
        discord.Color.purple(),
        discord.Color.gold(),
        discord.Color.magenta()
    ]

    embed = discord.Embed(
        title="🔥 이시진 기습숭배 🔥",
        description="""이시진은 2012년에 태어나 6974년에 죽은 완전생물입니다.
그를 표현할 수 있는 말은 그저 **GOAT**

만약 이 세상에 이시진 팬이 10억명이 있다면 나는 그 중 한명일것이다
만약 이 세상에 이시진 팬이 100명 있다면 나는 그 중 한명일것이다
만약 이 세상에 이시진 팬이 10명 있다면 나는 그 중 한명일것이다
만약 이 세상에 이시진 팬이 0명이라면 나는 이시진과 함께하는 상태일 것이다

그는 나의 삶의 의미 그 뿐""",
        color=random.choice(colors)
    )

    embed.add_field(
        name="현재 숭배자 수",
        value=f"{worship_count}명",
        inline=False
    )

    embed.set_footer(
        text=f"{interaction.user}님이 기습숭배 시전"
    )

    embed.set_thumbnail(
        url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(
        embed=embed,
        view=WorshipView()
    )


bot.run(os.getenv("DISCORD_TOKEN"))