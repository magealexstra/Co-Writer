from __future__ import annotations

import requests
from typing import Optional, Dict, Any


class CoWriter:
    """
    A class to interact with a local Language Model (LLM) for text generation.
    """

    def __init__(self, base_url: str = 'http://127.0.0.1:1234') -> None:
        """
        Initialize the CoWriter with the local LLM endpoint.

        :param base_url: URL of the local LLM server
        """
        self.base_url = base_url

    def generate_text(self, prompt: str, max_tokens: int = 150) -> Optional[str]:
        """
        Generate text using the local LLM.

        :param prompt: Input prompt for text generation
        :param max_tokens: Maximum number of tokens to generate
        :return: Generated text or None if request fails
        """
        try:
            response = requests.post(
                f'{self.base_url}/v1/chat/completions',
                json={
                    'messages': [{'role': 'user', 'content': prompt}],
                    'max_tokens': max_tokens
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except requests.RequestException as e:
            print(f"Error communicating with LLM: {e}")
            return None


def main() -> None:
    """
    Main function to demonstrate CoWriter functionality.
    """
    co_writer = CoWriter()
    prompt = "Write a short story about a programmer and an AI working together."
    result = co_writer.generate_text(prompt)

    if result:
        print("Generated Text:")
        print(result)


if __name__ == '__main__':
    main()
