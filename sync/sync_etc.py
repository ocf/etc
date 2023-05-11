import argparse
import logging
import os
import shutil
import time
from pathlib import Path
from subprocess import CalledProcessError
from subprocess import check_call


def get_cache_dir() -> Path:
    p = os.getenv(
        'OCF_CACHE_DIR', os.getenv(
        'XDG_CACHE_HOME', Path.home() / '.cache',
        ),
    )
    return Path(p).resolve() / 'ocf-etc'


def get_cached_repo(repo_url: str):
    cache_dir = get_cache_dir()

    def git(*args):
        return check_call(['git', *args], cwd=cache_dir)

    if cache_dir.exists():
        try:
            git('fetch', repo_url, 'HEAD', '--depth', '1')
            git('checkout', '--detach')
            git('reset', '--hard', 'FETCH_HEAD')
            git('clean', '-dfx')
        except CalledProcessError:
            shutil.rmtree(cache_dir)
        else:
            return cache_dir

    cache_dir.mkdir(exist_ok=True, parents=True)
    git('clone', repo_url, cache_dir)
    git('checkout', '--detach')

    return cache_dir


def update_etc(repo_url: str, repo_path: str, out_path: Path):
    if repo_path.is_absolute():
        repo_path = repo_path.relative_to('/')
    repo = get_cached_repo(repo_url)
    check_call([
        'rsync', '-rlpt', '--delete',
        f'{repo / repo_path}/', out_path,
    ])


def main():
    parser = argparse.ArgumentParser(
        description='Sync etc files from a git repo',
    )
    parser.add_argument('out_path', type=Path, default=Path('/etc/ocf'))
    parser.add_argument(
        '--repo-url', type=str,
        default='https://github.com/ocf/etc',
    )
    parser.add_argument('--repo-path', type=Path, default=Path('/configs'))
    parser.add_argument('--repeat-delay-secs', type=int, default=0)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

    if args.repeat_delay_secs > 0:
        while True:
            logging.log(logging.INFO, 'Updating etc files...')
            update_etc(args.repo_url, args.repo_path, args.out_path)
            time.sleep(args.repeat_delay_secs)
    else:
        update_etc(args.repo_url, args.repo_path, args.out_path)


if __name__ == '__main__':
    main()
