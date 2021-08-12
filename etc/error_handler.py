from discord import Embed


async def invalid_argument(self, ctx, command):
    """
    :param self:
    :param ctx:
    :param command:
    :return:

    Error Handler, Expandable
    """
    commands = {"rm_cycle": "<ID> or <ID, ID...>",
                "rmc": "<ID> or <ID, ID...>",
                "add_cycle": "<NAME>",
                "adc": "<NAME>"}

    # Embed Creation for the Error message
    embed = Embed(title="Ungültige Parameter",
                  description=f"Die Werte die du an den Command `!{command}` übergeben hast sind ungültig.",
                  color=0xCD5D7D)
    embed.add_field(name=f"Richtigen Parameter:", value=f"`{commands[command]}`", inline=True)

    await ctx.send(embed=embed)
