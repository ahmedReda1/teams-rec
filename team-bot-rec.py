import os
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity

adapter_settings = BotFrameworkAdapterSettings(
    appId=os.environ.get("03d17a10-6615-4460-a6b1-3d478f08a197"),
    appPassword=os.environ.get("Lmm8Q~8JMMu95JoGjKePAL0tyfv.lrev_i7p0a96")
)

adapter = BotFrameworkAdapter(adapter_settings)

async def on_message_activity(activity: Activity):
    if activity.type == "message":
        await adapter.send_activity(
            Activity(
                type="message",
                text=f"You said: {activity.text}"
            )
        )

bot = Bot(adapter, on_message_activity)

if __name__ == "__main__":
    bot.listen()