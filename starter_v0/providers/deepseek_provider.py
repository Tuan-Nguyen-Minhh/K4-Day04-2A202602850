from __future__ import annotations

import os
from typing import Any

from providers.openai_provider import OpenAIProvider


class DeepSeekProvider(OpenAIProvider):
    """DeepSeek's OpenAI-compatible Chat Completions provider."""

    def __init__(self) -> None:
        super().__init__(
            api_key_env="DEEPSEEK_API_KEY",
            base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            default_model=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"),
        )

    def complete(
        self,
        messages: list[dict[str, str]],
        tools: list[dict[str, Any]] | None = None,
        *,
        model: str | None = None,
        temperature: float = 0.0,
        tool_choice: Any | None = None,
    ):
        thinking = os.getenv("DEEPSEEK_THINKING", "disabled").strip().lower()
        if thinking not in {"enabled", "disabled"}:
            raise RuntimeError("DEEPSEEK_THINKING must be enabled or disabled")
        return super().complete(
            messages,
            tools,
            model=model,
            temperature=temperature,
            tool_choice=tool_choice,
            extra_body={"thinking": {"type": thinking}},
        )
