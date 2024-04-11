import os


def resource(relative_path):
    import itdvn_project_tests
    from pathlib import Path

    resources_path = (
        Path(itdvn_project_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .absolute()
    )

    if not os.path.isdir(resources_path):
        os.makedirs(resources_path)

    return (
        resources_path
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )


def path(relative_path):
    import itdvn_project_tests
    from pathlib import Path

    return (
        Path(itdvn_project_tests.__file__)
        .parent
        .joinpath('controls')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
