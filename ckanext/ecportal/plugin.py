'''
plugin.py
'''

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.ecportal.helpers as helpers

class ECPortalPlugin(plugins.SingletonPlugin):
    '''
	EC portal theme plugin.
    '''

    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

    # see the ITemplateHelpers plugin interface.
    def get_helpers(self):
        return {'most_viewed_datasets': helpers.most_viewed_datasets,
                'recent_updates': helpers.recent_updates,
                'top_publishers': helpers.top_publishers,
                'get_reference_dates_ec': helpers.get_reference_dates_ec,
                'from_json_ec': helpers.from_json_ec
               }



