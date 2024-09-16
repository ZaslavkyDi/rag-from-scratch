from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class LangfuseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LANGFUSE_")

    public_key: str | None
    secret_key: str | None
    host: str = "http://0.0.0.0:3000"

    @property
    def callback_handler(self):
        from langfuse.callback import CallbackHandler
        return CallbackHandler(
            public_key=self.public_key,
            secret_key=self.secret_key,
            host=self.host
        )


class OpenAISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OPENAI_")

    api_key: str | None
    model_name: str = "gpt-4o"


langfuse_settings = LangfuseSettings()
openai_settings = OpenAISettings()
