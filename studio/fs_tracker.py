"""Utilities to track and record file system."""

import os
import uuid

TFSTUDIO_MODEL_PATH = 'TFSTUDIO_MODEL_PATH'


def get_model_directory(experiment_name=None):
    if experiment_name:
        return os.path.join(
            os.path.expanduser('~'),
            '.tfstudio/models/',
            experiment_name)
    else:
        if TFSTUDIO_MODEL_PATH not in os.environ.keys():
            # this bit should only be excuted when running outside
            # studio-runner
            setup_model_directory(os.environ, str(uuid.uuid4()))
        return os.environ[TFSTUDIO_MODEL_PATH]


def setup_model_directory(env, experiment_name):
    path = get_model_directory(experiment_name)
    if not os.path.exists(path):
        os.makedirs(path)
    env[TFSTUDIO_MODEL_PATH] = path


def get_queue_directory():
    queue_dir = os.path.join(os.path.expanduser('~'),
                        '.tfstudio/queue')
    if not os.path.exists(queue_dir):
        os.makedirs(queue_dir)

    return queue_dir