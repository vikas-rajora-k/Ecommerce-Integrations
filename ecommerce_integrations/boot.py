try:
	from ecommerce_integrations.shopify.constants import OLD_SETTINGS_DOCTYPE
except ModuleNotFoundError:
	OLD_SETTINGS_DOCTYPE = None


def boot_session(bootinfo):
	"""Don't show old doctypes after enabling new ones."""
	if not OLD_SETTINGS_DOCTYPE:
		return

	try:
		bootinfo.single_types.remove(OLD_SETTINGS_DOCTYPE)
	except ValueError:
		pass
