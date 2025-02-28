from .lora import modify_with_lora
from .adapters import modify_with_adapters
from .bitfit import modify_with_bitfit
from .prompt_tuning import modify_with_prompt_tuning
from .intrinsic import modify_with_intrinsic_model

modifier_dict = {
    "lora": modify_with_lora,
    "bitfit": modify_with_bitfit,
    "adapters": modify_with_adapters,
    "prompt-tuning": modify_with_prompt_tuning,
    "intrinsic": modify_with_intrinsic_model,
}


def modify_transformer(transformer, config):
    if config.model_modifier:
        if config.model_modifier in modifier_dict:
            transformer = modifier_dict[config.model_modifier](transformer, config)
        else:
            raise ValueError(f"Model modifier '{config.model_modifier}' not found.")

    return transformer
