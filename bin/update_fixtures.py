#!/usr/bin/env python
import json
import os

def document_model(type, data, pk, model='info.document'):
    return {
        'model': model,
        'pk': pk,
        'fields': {
            'type': type,
            'data': data
        }
    }

if __name__ == '__main__':

    docs = ('bonusmissions.md', 'dieselrules.md')
    docs_path = os.path.join(os.curdir, 'docs')
    fixtures = []

    if not os.path.exists(docs_path):
        raise IOError(
            "%s is not a valid path. Run using ./bin/update_fixtures" % target
        )

    for idx, doc in enumerate(docs):
        idx += 1
        fname = os.path.join(docs_path, doc)
        with open(fname) as f:
            data = ' '.join([line for line in f])
        if idx == 1:
            dtype = 'bonus',
        else:
            dtype = 'rules'
        fixtures.append(document_model(dtype, data, idx))

    
    # TODO: write directly to appname/fixtures/
    # write to file in project_root.
    target_path = os.path.join(
        os.path.dirname(docs_path), 'dieselsite', 'info', 'fixtures',
    )
    fname = os.path.join(target_path, 'initial_data.json')
    with open(fname, 'w') as f:
        json.dump(fixtures, f)
