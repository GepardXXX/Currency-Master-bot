from aiogram import Router

from . import (
    back_button_handler,
    currency_conversion,
    currency_rate,
    default_commands,
    processing_the_amount_input,
)


def setup_routers() -> Router:
    router = Router()

    router.include_routers(
        default_commands.router,
        currency_rate.router,
        back_button_handler.router,
        currency_conversion.router,
        processing_the_amount_input.router,
    )
    return router
