import starkbank


class SettingUserClass:
    # This is only an example of a private key content. You should use your own key.
    private_key_content = "your privateKey here"

    # for project users:
    user = starkbank.Project(
        environment="sandbox",
        id="your idProject here",
        private_key=private_key_content
    )

    starkbank.user = user
