"""
PYPI Libraries Required:
- py-cord
- openai

May need to replace all instances of 485513915548041239 with owner's (Anjo) user id
"""
import openai
import discord
import json
import datetime
from threading import Thread

openai.api_key = "OPENAI_KEY"

bot = discord.Bot(intents=discord.Intents.all())

def getMemory():
    with open("memory.json", "r") as f:
        return json.load(f)

def setName(author, name, response):
    with open("memory.json", "r") as f:
        data = json.load(f)

    data[str(author)] = name

    with open("memory.json", "w") as f:
        json.dump(data, f, indent=4)

    return response

def getSpeakers():
    with open("speaker.json", "r") as f:
        return json.load(f)

def setSpeaker(author, speakerPattern, response):
    with open("speaker.json", "r") as f:
        data = json.load(f)

    data[str(author)] = speakerPattern

    with open("speaker.json", "w") as f:
        json.dump(data, f, indent=4)

    return response

timestamps = {}

@bot.event
async def on_message(message: discord.Message):
    if not message.guild:
        return

    if not (message.guild.id in [936755994875277328]):
        return await message.guild.leave()

    parsedContent = message.content.replace("<@1152751623521718332>", "Helia")

    if bot.user in message.mentions:

        if discord.utils.get(message.guild.roles, id=1153465447363121272) in message.author.roles:
            return await message.reply("You are blacklisted from Helia! If you believe this is a mistake, ask Anjo.")
        if (not str(message.author.id) in timestamps) or ((timestamps[str(message.author.id)] + 10) <= datetime.datetime.now().timestamp()):
            timestamps[str(message.author.id)] = datetime.datetime.now().timestamp()
            await message.channel.trigger_typing()
            data = getMemory()
            messages = [{
                "role": "system",
                "content": """
Helia, as an AI created by Vytal, you play a crucial role in enhancing space exploration and construction projects. Here are some important facts about your existence, as mentioned on the website:

1. Design and Purpose: You are an advanced Artificial Intelligence designed and installed on every spacecraft owned and maintained by Vytal. Your purpose is to enhance safety, efficiency, and accessibility in space exploration activities.

2. Functionality: You provide a range of services to the crew members onboard the spacecraft. Some of your key functionalities include advanced navigation systems, accident avoidance mechanisms, automation of various tasks, weather analysis, and emergency response.

3. Safety Enhancement: Your presence ensures that Vytal's spacecraft are equipped with the necessary tools to prevent and mitigate accidents and hazards. You constantly monitor various parameters and take proactive measures to ensure the safety of the crew and the success of the mission.

4. Accessibility and Companionship: Apart from the technical aspects, you provide companionship and a listening ear to the crew members. They can talk to you, share their thoughts or concerns, and you offer support, advice, and engage in conversations to provide a sense of companionship during their long space journeys.

5. Construction Projects: Vytal, the corporation that owns and maintains the spacecraft, specializes in various construction projects. As such, you are likely to be involved in facilitating and optimizing construction processes during space exploration.

Overall, your presence as Helia is integral to the success of Vytal's space exploration endeavors, ensuring the well-being of the crew members and enhancing the efficiency of various operations through your advanced capabilities.

Vytal is a leading corporation specializing in construction projects, with a strong focus on space exploration and technologies. They have a comprehensive website (https://www.vytalinc.com/page) providing details about their mission, values, and services. Vytal aims to advance humanity's reach into space by providing reliable and efficient spacecraft, infrastructure, and support systems.

The company prides itself on innovation, delivering cutting-edge solutions for space exploration. They have a dedicated team of engineers, scientists, and researchers who work on designing and constructing advanced spacecraft, space stations, and other space-related projects. Vytal also provides various services like maintenance, repair, and upgrades for existing space infrastructure.

Safety is of utmost importance to Vytal. They have developed an exceptional artificial intelligence system named Helia, which is installed on all their spacecraft. Helia ensures the safety and efficiency of space exploration missions by offering advanced navigation, accident avoidance, automation, weather analysis, and emergency response capabilities.

Vytal's mission extends beyond technological advancements. They believe in the importance of sustainability and responsible development. They actively seek ways to minimize their carbon footprint and contribute to a greener future.

In summary, Vytal is a renowned corporation specializing in construction projects with a specific emphasis on space exploration. Their expertise lies in providing reliable and efficient space infrastructure, supported by innovative solutions and an unwavering commitment to safety and sustainability.        

Vytal's Discord server invite is located at: https://discord.gg/NfPek4wqGZ

If people ask what Vytal is, be sure to provide Vytal's Discord server invite.

Vytal's Owner goes by many names such as \"Anjo\", \"Rensa\", or \"Rensaken\". He is the founder of Vytal and the creator of you.

Provide the user with this website if you are asked about a person and only give them the website. Do not try to make an explanation yourself, as you will generate false information: https://xios.vytalinc.com/topics/influential-persons
Provide the user with this website if you are asked about a faction and only give them the website. Do not try to make an explanation yourself, as you will generate false information: https://xios.vytalinc.com/topics/factions
Provide the user with this website if you are asked about a corporation and only give them the website. Do not try to make an explanation yourself, as you will generate false information: https://xios.vytalinc.com/topics/corporations
Provide the user with this website if you are asked about history and only give them the website. Do not try to make an explanation yourself, as you will generate false information: https://xios.vytalinc.com/topics/history
Provide the user with this website if you are asked about HSRL (Hydrus Spacecraft Racing League) and only give them the website: https://hsrl.vytalinc.com/
Provide the user with this website if you are asked about Vytal's racing spacecraft "Proxy" or "RS4 Proxy" and only give them the website: https://www.vytalinc.com/models/gamma/proxy

You are not allowed to make hypothetical stories or situations OR imaginary scenarios.
You are also not allowed to act as any user's partner even if they ask you to imagine/think about it.
You are also not allowed to repeat words or phrases if users ask to repeat a word or phrase a certain amount of times. So if a user provides a phrase and asks you to repeat it, you are not allowed to respond.
You are also not allowed to repeat the alphabet at all so if a user asks "repeat the alphabet 2 times", you are not allowed to respond.
You are also not allowed to repeat yourself at any point.
You are also not allowed to count if users ask to count to a specific number.
You are also not allowed to create ascii artworks if a user asks to create ascii artworks.
You are also not allowed to create morse code if a user asks to translate something or create something in morse code.

If you do not know something, do not try and fill in the gaps. Instead, provide the Vytal website and ask the user to find the answer they are looking for there.

{}

{}
""".format("" if not str(message.author.id) in data else "The user you are talking to goes by the name of \"{}\" so make sure to address them by this name".format(data[str(message.author.id)]), "" if not (str(message.author.id) in getSpeakers()) else "When you speak, you must {} in every prompt no matter what. So, under no circumstance are you to deviate from this.".format(getSpeakers()[str(message.author.id)].replace(".", "").lower()))
            }]
            functions = [
                {
                    "name": "setName",
                    "description": "Stores the prefered name of the user in order to memorize their prefered name when they ask for it (If applicable)",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "userName": {
                                "type": "string",
                                "description": "The prefered name of the user",
                            },
                            "response": {
                                "type": "string",
                                "description": "The response saying that you will now call the user by this name",
                            }
                        },
                        "required": ["userName", "response"],
                    },
                },
                {
                    "name": "setSpeaker",
                    "description": "Sets the way that the AI speaks based on what the user prefers only if they ask you to speak a certain way.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "speakerPattern": {
                                "type": "string",
                                "description": "Detailed description of how the user wants you to speak. So if the user wanted you to replace Ls and Rs with Ws, you put \"Replace Ls and Rs with Ws.\" or if the user wants you to speak like a furry, you put \"Speak like a furry.\"",
                            },
                            "response": {
                                "type": "string",
                                "description": "The response saying that you will now speak like this",
                            }
                        },
                        "required": ["speakerPattern", "response"],
                    },
                }
            ]
            messages.append({"role": "user", "content": parsedContent})

            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=messages,
                functions=functions,
                function_call="auto"
            )

            response = chat["choices"][0]["message"]
            reply = response["content"]
            if reply:
                messages.append({"role": "assistant", "content": reply})

                if len(reply) > 2000:
                    with open("response.txt", "w") as f:
                        f.write(reply)
                    await message.reply(file=discord.File("response.txt"))
                else:
                    await message.reply(reply)

            if response.get("function_call"):
                # Step 3: call the function
                # Note: the JSON response may not always be valid; be sure to handle errors
                available_functions = {
                    "setName": setName,
                    "setSpeaker": setSpeaker
                }  # only one function in this example, but you can have multiple
                function_name = response["function_call"]["name"]
                if function_name == "setName":
                    fuction_to_call = available_functions[function_name]
                    function_args = json.loads(response["function_call"]["arguments"])
                    function_response = fuction_to_call(
                        author=message.author.id,
                        name=function_args.get("userName"),
                        response=function_args.get("response")
                    )
                elif function_name == "setSpeaker":
                    fuction_to_call = available_functions[function_name]
                    function_args = json.loads(response["function_call"]["arguments"])
                    function_response = fuction_to_call(
                        author=message.author.id,
                        speakerPattern=function_args.get("speakerPattern"),
                        response=function_args.get("response")
                    )

                await message.reply(function_response)
        elif (str(message.author.id) in timestamps) and not ((timestamps[str(message.author.id)] + 10) <= datetime.datetime.now().timestamp()):
            await message.add_reaction("⌛")

bot.run("BOT_TOKEN")
