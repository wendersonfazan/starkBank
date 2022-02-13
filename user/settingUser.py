import starkbank


class SettingUserClass:
    # This is only an example of a private key content. You should use your own key.
    private_key_content = """
    -----BEGIN EC PARAMETERS-----
    BgUrgQQACg==
    -----END EC PARAMETERS-----
    -----BEGIN EC PRIVATE KEY-----
    MHQCAQEEIK45++UeTan44MqXmIR+re67lRmk/vgn7b0ttOPAUQQyoAcGBSuBBAAK
    oUQDQgAEnLqgdo9teZwe5uZSaFCJceGdt8KbJ6c+36rCK9XdqtvQjrWQCHDPnwJ4
    upLGDwSdRqVrNCIzjU14VPPDDFLeuw==
    -----END EC PRIVATE KEY-----
    """

    # for project users:
    user = starkbank.Project(
        environment="sandbox",
        id="4958663127072768",
        private_key=private_key_content
    )

    starkbank.user = user
