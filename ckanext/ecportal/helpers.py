import logging
import operator

import ckan
import ckan.model as model
import ckan.plugins as p
import ckan.lib.search as search
import ckan.lib.helpers as h

NUM_TOP_PUBLISHERS = 6
NUM_MOST_VIEWED_DATASETS = 10

log = logging.getLogger(__file__)


def recent_updates(n):
    '''
    Return a list of the n most recently updated datasets.
    '''
    context = {'model': model,
               'session': model.Session,
               'user': p.toolkit.c.user or p.toolkit.c.author}
    data = {'rows': n,
            'sort': u'modified_date desc',
            'facet': u'false',
            'fq': u'capacity: "public"'}
    try:
        search_results = p.toolkit.get_action('package_search')(context, data)
    except search.SearchError:
        log.error('Error searching for recently updated datasets')
        log.error(e)
        search_results = {}

    log.error('Found %d recent updates ' % len(search_results))
#    log.error('Updates:  %r ' % search_results)
    return search_results.get('results', [])


def top_publishers():
    '''
    Updates the 'packages' field in each group dict (up to a maximum
    of NUM_TOP_PUBLISHERS) to show the number of public datasets in the group.
    '''
##    orgs = [g for g in groups if g['packages'] > 0]
#    orgs = [Organization(name='org1', Organization )]
#    publishers.sort(key=operator.itemgetter('packages'), reverse=True)

#    return publishers[:NUM_TOP_PUBLISHERS]
    context = {'model': model,
               'session': model.Session,
               'user': p.toolkit.c.user or p.toolkit.c.author}
    data = {'sort': u'packages desc',
            'all_fields': u'true'}
    try:
        search_results = p.toolkit.get_action('organization_list')(context, data)
    except search.SearchError:
        log.error('Error searching for top orgs')
        log.error(e)
        search_results = {}

    log.error('Found %d top orgs' % len(search_results))
    #log.error('Top orgs %r' % search_results)
    return search_results



def OLDmost_viewed_datasets(num_datasets=NUM_MOST_VIEWED_DATASETS):
    try:
        data = {'rows': num_datasets,
                'sort': u'views_total desc',
                'facet': u'false',
                'fq': u'capacity: "public"',
                'fl': 'id, name, title, views_total'}
        # Ugly: going through ckan.lib.search directly
        # (instead of get_action('package_search').
        #
        # TODO: Can we return views_total using package_search for internal
        # use only (without outputting it during public API calls)?
        query = search.query_for(model.Package)
        result = query.run(data)
        log.error('found %d datasets. Filtering most viewed...' % len(result))
        log.error('dataset: %r' % result )

        return [r for r in result.get('results', [])
                if r.get('tracking_summary',{}).get('total',0) > 0]
    except search.SearchError, e:
        log.error('Error searching for most viewed datasets')
        log.error(e)

def most_viewed_datasets(n=NUM_MOST_VIEWED_DATASETS):
    '''
    Return a list of the n most recently updated datasets.
    '''
    context = {'model': model,
               'session': model.Session,
               'user': p.toolkit.c.user or p.toolkit.c.author}
    data = {'rows': n,
            'sort': u'views_total desc',
            'facet': u'false',
            'fq': u'capacity: "public"'}
    try:
        search_results = p.toolkit.get_action('package_search')(context, data)
    except search.SearchError:
        log.error('Error searching for most viewed datasets')
        log.error(e)
        search_results = {}

    log.error('Found %d most viewed updates ' % len(search_results))
    return [r for r in search_results.get('results', [])
                       if r.get('tracking_summary',{}).get('total',0) > 0]

#    log.error('Updates:  %r ' % search_results)
    return search_results.get('results', [])


def get_reference_dates_ec(date_str):
    '''
        Gets a reference date extra created by the harvesters and formats it
        nicely for the UI.

        Examples:
            [{"type": "creation", "value": "1977"}, {"type": "revision", "value": "1981-05-15"}]
            [{"type": "publication", "value": "1977"}]
            [{"type": "publication", "value": "NaN-NaN-NaN"}]

        Results
            1977 (creation), May 15, 1981 (revision)
            1977 (publication)
            NaN-NaN-NaN (publication)
    '''
    try:
        out = {}
        for date in h.json.loads(date_str):              
            value = h.render_datetime(date['value']) or date['value']
            out[date['type']] = value
        return out
    except (ValueError, TypeError):
        return None

def from_json_ec(str):
    try:
        return h.json.loads(str)
    except (ValueError, TypeError):
        return None

