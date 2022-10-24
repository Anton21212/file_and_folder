import os
from pathlib import Path

from django.http import JsonResponse
from django.views import View

from config.config import API_SEARCHED_DIRECTORY


class MetaView(View):
    def get(self, request):
        base_path = API_SEARCHED_DIRECTORY
        files_and_dirs_meta = _get_files_and_dirs_meta(base_path)
        result = {
            'data': files_and_dirs_meta,
        }
        return JsonResponse(result)


def _get_files_and_dirs_meta(base_path: Path):
    result = []
    for path in base_path.iterdir():
        obj_info = dict()
        obj_info['name'] = path.name
        if path.is_dir():
            obj_info['type'] = 'folder'
        else:
            obj_info['type'] = 'file'
        stat = os.stat(path)
        try:
            creation_time = stat.st_birthtime
        except AttributeError:
            creation_time = stat.st_ctime
        time = int(creation_time * 1000)
        obj_info['time'] = time
        result.append(obj_info)
    return result
