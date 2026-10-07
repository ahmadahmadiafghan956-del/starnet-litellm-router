# StarNet LiteLLM Router

Experimental LiteLLM proxy for StarNet.

Secrets are not stored in this repository. Configure provider API keys and `LITELLM_MASTER_KEY` only as Render environment variables.

Render:
- Build: `pip install -r requirements.txt`
- Start: `litellm --config config.yaml --port $PORT`
