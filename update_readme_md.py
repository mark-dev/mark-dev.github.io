#! /usr/bin/env python3

import collections
import logging
import os
import pathlib
from datetime import timedelta, datetime

CWD = os.getcwd()


def get_update_date(file_path):
    unix_time = os.path.getmtime(file_path)
    msk_dt = unix_time + timedelta(hours=3).total_seconds()
    return datetime.utcfromtimestamp(msk_dt).strftime('%Y-%m-%d')


def main():
    logging.basicConfig(level=logging.INFO)

    date_to_paths = collections.defaultdict(list)

    paths = pathlib.Path(CWD).rglob('**/*.html')
    for p in paths:
        update_date = get_update_date(p.absolute())
        date_to_paths[update_date].append(p)

    known_dates = list(date_to_paths.keys())
    known_dates.sort(reverse=True)

    logging.info(known_dates)

    cwd_dir = pathlib.Path(CWD)
    today = str(datetime.today().date())
    today_links = []
    markdown_parts = []
    for dt in known_dates:
        dt_paths = date_to_paths[dt]
        if dt_paths:
            markdown_parts.append(f'# {dt}')
            for pp in dt_paths:
                rel_path = str(pp.relative_to(CWD))
                if today == dt:
                    today_links.append(f'https://mark-dev.github.io/{rel_path}')
                markdown_parts.append(f'<a href="{rel_path}">{pp.name}</a><br>')
            markdown_parts.append('---')
    new_markdown = '\n'.join(markdown_parts)

    readme_file = (cwd_dir / 'README.md')
    if readme_file.exists():
        readme_file.write_text(new_markdown)
    if today_links:
        logging.info('See also today links:\n%s', '\n'.join(today_links))


if __name__ == '__main__':
    main()
