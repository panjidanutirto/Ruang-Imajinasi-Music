from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hei, saya **{bn}** !!
Saya bisa memutar musik di panggilan suara grup anda. Dikembangkan oleh @haimaspann.

Tambahkan saya ke grup Anda dan mainkan musik dengan bebas!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 Perintah", url="https://telegra.ph/Ruang-Imajinasi-Music----Command-04-21"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url="https://t.me/RuangImajinasiGroup"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url="https://t.me/RI_Channel_Official"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎁 Donasi", url="https://t.me/haimaspann"
                    )
                ],
            ]
        )
    )
