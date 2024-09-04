from rss_receiver import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if rss_receiver is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IRssReceiverLayer is registered."""
        from rss_receiver.interfaces import IRssReceiverLayer

        assert IRssReceiverLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240904001"
