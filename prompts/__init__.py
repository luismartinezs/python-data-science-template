from .spr_generator import spr_generator
from .spr_decompressor import spr_decompressor

prompts = {
    "spr_generator": spr_generator,
    "spr_decompressor": spr_decompressor,
}

__all__ = ["prompts"]
