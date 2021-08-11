from discord import Embed


async def invalid_argument(self, ctx, command):
    commands = {"!rm_cycle": "<ID>",
                "!rmc": "<ID>"}

    embed = Embed(title="Ungültige Parameter",
                  description=f"Die Werte die du an den Command !`{command}` übergeben hast sind ungültig.",
                  color=0x1acdee)
    embed.add_field(name=f"Richtigen Parameter:", value=f"`{commands[command]}`", inline=True)

    await ctx.send(embed=embed)
