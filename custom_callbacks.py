from litellm.integrations.custom_logger import CustomLogger

class StarNetRequestNormalizer(CustomLogger):
    async def async_pre_call_hook(self, user_api_key_dict, cache, data, call_type):
        # StarNet can request a very large output budget. Keep free providers usable.
        requested = data.get("max_tokens")
        if requested is None or requested > 2000:
            data["max_tokens"] = 2000

        # Some providers reject StarNet's non-standard per-message timestamp field.
        messages = data.get("messages")
        if isinstance(messages, list):
            cleaned = []
            for message in messages:
                if isinstance(message, dict):
                    message = dict(message)
                    message.pop("ts", None)
                cleaned.append(message)
            data["messages"] = cleaned
        return data

proxy_handler_instance = StarNetRequestNormalizer()
