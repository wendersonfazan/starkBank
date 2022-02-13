import starkbank


class SettingUserClass:
    # This is only an example of a private key content. You should use your own key.
    private_key_content = ""

    # for project users:
    user = starkbank.Project(
        environment="sandbox",
        id="4958663127072768",
        private_key=private_key_content
    )

    starkbank.user = user
