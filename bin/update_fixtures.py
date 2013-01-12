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
    target_path = os.path.join(os.curdir, 'docs')
    fixtures = []

    if not os.path.exists(target_path):
        raise IOError(
            "%s is not a valid path. Run using ./bin/update_fixtures" % target
        )

    for idx, doc in enumerate(docs):
        idx += 1
        fname = os.path.join(target_path, doc)
        with open(fname) as f:
            data = ' '.join([line.strip() for line in f])
        if idx == 1:
            dtype = 'bonus',
        else:
            dtype = 'rules'
        fixtures.append(document_model(dtype, data, idx))

    
    # TODO: write directly to appname/fixtures/
    # write to file in project_root.
    fname = os.path.join(os.path.dirname(target_path), 'documents')
    with open(fname, 'w') as f:
        f.write(json.dumps(fixtures))
