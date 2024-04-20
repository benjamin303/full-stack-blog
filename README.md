# full-stack-blog
This blog app is build using React JS, Django and MySQL.
```
full-stack-blog
├─ backend
│  ├─ blog
│  │  ├─ blog
│  │  │  ├─ asgi.py
│  │  │  ├─ settings.py
│  │  │  ├─ urls.py
│  │  │  ├─ wsgi.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ settings.cpython-39.pyc
│  │  │     ├─ urls.cpython-39.pyc
│  │  │     ├─ wsgi.cpython-39.pyc
│  │  │     └─ __init__.cpython-39.pyc
│  │  ├─ db.sqlite3
│  │  ├─ home
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ migrations
│  │  │  │  ├─ __init__.py
│  │  │  │  └─ __pycache__
│  │  │  │     └─ __init__.cpython-39.pyc
│  │  │  ├─ models.py
│  │  │  ├─ static
│  │  │  │  └─ css
│  │  │  │     └─ style.css
│  │  │  ├─ templates
│  │  │  │  └─ home.html
│  │  │  ├─ tests.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ admin.cpython-39.pyc
│  │  │     ├─ apps.cpython-39.pyc
│  │  │     ├─ models.cpython-39.pyc
│  │  │     ├─ urls.cpython-39.pyc
│  │  │     ├─ views.cpython-39.pyc
│  │  │     └─ __init__.cpython-39.pyc
│  │  ├─ manage.py
│  │  ├─ media
│  │  │  ├─ post_images
│  │  │  │  ├─ 2021-bmw-m4-x3-1920x1080.jpg
│  │  │  │  ├─ 2022-bmw-m4-gt4-front-10k-xn-1920x1080.jpg
│  │  │  │  ├─ 2022-suzuki-hayabusa-on-track-dg-1920x1080.jpg
│  │  │  │  ├─ atv-motocross-1920x1080.jpg
│  │  │  │  ├─ biker-burnout-4k-xv-1920x1080.jpg
│  │  │  │  └─ biker-donut-4k-si-1920x1080.jpg
│  │  │  └─ user_profiles
│  │  │     ├─ 2016-BMW-M2-Coupe-015-2000-scaled.jpg
│  │  │     └─ 2018-ducati-panigale-v4-4k-3j-1920x1080.jpg
│  │  ├─ posts
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ forms.py
│  │  │  ├─ migrations
│  │  │  │  ├─ 0001_initial.py
│  │  │  │  ├─ 0002_remove_post_author.py
│  │  │  │  ├─ 0003_alter_post_id.py
│  │  │  │  ├─ 0004_auto_20230713_1747.py
│  │  │  │  ├─ 0005_auto_20230713_1757.py
│  │  │  │  ├─ 0006_auto_20230713_1815.py
│  │  │  │  ├─ 0007_post_keywords.py
│  │  │  │  ├─ 0008_auto_20230719_1003.py
│  │  │  │  ├─ __init__.py
│  │  │  │  └─ __pycache__
│  │  │  │     ├─ 0001_initial.cpython-39.pyc
│  │  │  │     ├─ 0002_remove_post_author.cpython-39.pyc
│  │  │  │     ├─ 0003_alter_post_id.cpython-39.pyc
│  │  │  │     ├─ 0004_auto_20230713_1747.cpython-39.pyc
│  │  │  │     ├─ 0005_auto_20230713_1757.cpython-39.pyc
│  │  │  │     ├─ 0006_auto_20230713_1815.cpython-39.pyc
│  │  │  │     ├─ 0007_post_keywords.cpython-39.pyc
│  │  │  │     ├─ 0008_auto_20230719_1003.cpython-39.pyc
│  │  │  │     └─ __init__.cpython-39.pyc
│  │  │  ├─ models.py
│  │  │  ├─ serializers.py
│  │  │  ├─ templates
│  │  │  │  ├─ 404.html
│  │  │  │  ├─ all_posts.html
│  │  │  │  ├─ create_post.html
│  │  │  │  ├─ edit_post.html
│  │  │  │  ├─ main.html
│  │  │  │  ├─ master.html
│  │  │  │  └─ post_details.html
│  │  │  ├─ tests.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ admin.cpython-39.pyc
│  │  │     ├─ apps.cpython-39.pyc
│  │  │     ├─ forms.cpython-39.pyc
│  │  │     ├─ models.cpython-39.pyc
│  │  │     ├─ serializers.cpython-39.pyc
│  │  │     ├─ urls.cpython-39.pyc
│  │  │     ├─ views.cpython-39.pyc
│  │  │     └─ __init__.cpython-39.pyc
│  │  ├─ static
│  │  │  └─ css
│  │  │     ├─ styles.css
│  │  │     └─ variables.css
│  │  └─ users
│  │     ├─ admin.py
│  │     ├─ apps.py
│  │     ├─ forms.py
│  │     ├─ migrations
│  │     │  ├─ 0001_initial.py
│  │     │  ├─ 0002_auto_20230711_2338.py
│  │     │  ├─ 0003_alter_user_id.py
│  │     │  ├─ 0004_user_slug.py
│  │     │  ├─ 0005_auto_20230713_1816.py
│  │     │  ├─ 0006_remove_user_slug.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ 0001_initial.cpython-39.pyc
│  │     │     ├─ 0002_auto_20230711_2338.cpython-39.pyc
│  │     │     ├─ 0003_alter_user_id.cpython-39.pyc
│  │     │     ├─ 0004_user_slug.cpython-39.pyc
│  │     │     ├─ 0005_auto_20230713_1816.cpython-39.pyc
│  │     │     ├─ 0006_remove_user_slug.cpython-39.pyc
│  │     │     ├─ 0007_auto_20230714_1709.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ models.py
│  │     ├─ serializers.py
│  │     ├─ templates
│  │     │  ├─ 404.html
│  │     │  ├─ all_users.html
│  │     │  ├─ create_user.html
│  │     │  ├─ edit_user.html
│  │     │  ├─ main.html
│  │     │  ├─ master.html
│  │     │  ├─ myfirst.html
│  │     │  └─ user_details.html
│  │     ├─ tests.py
│  │     ├─ urls.py
│  │     ├─ views.py
│  │     ├─ __init__.py
│  │     └─ __pycache__
│  │        ├─ admin.cpython-39.pyc
│  │        ├─ apps.cpython-39.pyc
│  │        ├─ forms.cpython-39.pyc
│  │        ├─ models.cpython-39.pyc
│  │        ├─ serializers.cpython-39.pyc
│  │        ├─ urls.cpython-39.pyc
│  │        ├─ views.cpython-39.pyc
│  │        └─ __init__.cpython-39.pyc
│  ├─ Include
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ distutils-precedence.pth
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autocompletion.cpython-39.pyc
│  │     │  │  │     ├─ base_command.cpython-39.pyc
│  │     │  │  │     ├─ cmdoptions.cpython-39.pyc
│  │     │  │  │     ├─ command_context.cpython-39.pyc
│  │     │  │  │     ├─ main.cpython-39.pyc
│  │     │  │  │     ├─ main_parser.cpython-39.pyc
│  │     │  │  │     ├─ parser.cpython-39.pyc
│  │     │  │  │     ├─ progress_bars.cpython-39.pyc
│  │     │  │  │     ├─ req_command.cpython-39.pyc
│  │     │  │  │     ├─ spinners.cpython-39.pyc
│  │     │  │  │     ├─ status_codes.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ completion.cpython-39.pyc
│  │     │  │  │     ├─ configuration.cpython-39.pyc
│  │     │  │  │     ├─ debug.cpython-39.pyc
│  │     │  │  │     ├─ download.cpython-39.pyc
│  │     │  │  │     ├─ freeze.cpython-39.pyc
│  │     │  │  │     ├─ hash.cpython-39.pyc
│  │     │  │  │     ├─ help.cpython-39.pyc
│  │     │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │     ├─ install.cpython-39.pyc
│  │     │  │  │     ├─ list.cpython-39.pyc
│  │     │  │  │     ├─ search.cpython-39.pyc
│  │     │  │  │     ├─ show.cpython-39.pyc
│  │     │  │  │     ├─ uninstall.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ installed.cpython-39.pyc
│  │     │  │  │     ├─ sdist.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ collector.cpython-39.pyc
│  │     │  │  │     ├─ package_finder.cpython-39.pyc
│  │     │  │  │     ├─ sources.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ _distutils.cpython-39.pyc
│  │     │  │  │     ├─ _sysconfig.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ candidate.cpython-39.pyc
│  │     │  │  │     ├─ direct_url.cpython-39.pyc
│  │     │  │  │     ├─ format_control.cpython-39.pyc
│  │     │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │     ├─ link.cpython-39.pyc
│  │     │  │  │     ├─ scheme.cpython-39.pyc
│  │     │  │  │     ├─ search_scope.cpython-39.pyc
│  │     │  │  │     ├─ selection_prefs.cpython-39.pyc
│  │     │  │  │     ├─ target_python.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auth.cpython-39.pyc
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ download.cpython-39.pyc
│  │     │  │  │     ├─ lazy_wheel.cpython-39.pyc
│  │     │  │  │     ├─ session.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ xmlrpc.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ metadata.cpython-39.pyc
│  │     │  │  │  │     ├─ metadata_editable.cpython-39.pyc
│  │     │  │  │  │     ├─ metadata_legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel_editable.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel_legacy.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  ├─ legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ editable_legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ legacy.cpython-39.pyc
│  │     │  │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ freeze.cpython-39.pyc
│  │     │  │  │     ├─ prepare.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_tracker.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constructors.cpython-39.pyc
│  │     │  │  │     ├─ req_file.cpython-39.pyc
│  │     │  │  │     ├─ req_install.cpython-39.pyc
│  │     │  │  │     ├─ req_set.cpython-39.pyc
│  │     │  │  │     ├─ req_tracker.cpython-39.pyc
│  │     │  │  │     ├─ req_uninstall.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ resolver.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ candidates.cpython-39.pyc
│  │     │  │  │  │     ├─ factory.cpython-39.pyc
│  │     │  │  │  │     ├─ found_candidates.cpython-39.pyc
│  │     │  │  │  │     ├─ provider.cpython-39.pyc
│  │     │  │  │  │     ├─ reporter.cpython-39.pyc
│  │     │  │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │  │     ├─ resolver.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ distutils_args.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ inject_securetransport.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ compatibility_tags.cpython-39.pyc
│  │     │  │  │     ├─ datetime.cpython-39.pyc
│  │     │  │  │     ├─ deprecation.cpython-39.pyc
│  │     │  │  │     ├─ direct_url_helpers.cpython-39.pyc
│  │     │  │  │     ├─ distutils_args.cpython-39.pyc
│  │     │  │  │     ├─ egg_link.cpython-39.pyc
│  │     │  │  │     ├─ encoding.cpython-39.pyc
│  │     │  │  │     ├─ entrypoints.cpython-39.pyc
│  │     │  │  │     ├─ filesystem.cpython-39.pyc
│  │     │  │  │     ├─ filetypes.cpython-39.pyc
│  │     │  │  │     ├─ glibc.cpython-39.pyc
│  │     │  │  │     ├─ hashes.cpython-39.pyc
│  │     │  │  │     ├─ inject_securetransport.cpython-39.pyc
│  │     │  │  │     ├─ logging.cpython-39.pyc
│  │     │  │  │     ├─ misc.cpython-39.pyc
│  │     │  │  │     ├─ models.cpython-39.pyc
│  │     │  │  │     ├─ packaging.cpython-39.pyc
│  │     │  │  │     ├─ setuptools_build.cpython-39.pyc
│  │     │  │  │     ├─ subprocess.cpython-39.pyc
│  │     │  │  │     ├─ temp_dir.cpython-39.pyc
│  │     │  │  │     ├─ unpacking.cpython-39.pyc
│  │     │  │  │     ├─ urls.cpython-39.pyc
│  │     │  │  │     ├─ virtualenv.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     ├─ _log.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bazaar.cpython-39.pyc
│  │     │  │  │     ├─ git.cpython-39.pyc
│  │     │  │  │     ├─ mercurial.cpython-39.pyc
│  │     │  │  │     ├─ subversion.cpython-39.pyc
│  │     │  │  │     ├─ versioncontrol.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build_env.cpython-39.pyc
│  │     │  │     ├─ cache.cpython-39.pyc
│  │     │  │     ├─ configuration.cpython-39.pyc
│  │     │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │     ├─ main.cpython-39.pyc
│  │     │  │     ├─ pyproject.cpython-39.pyc
│  │     │  │     ├─ self_outdated_check.cpython-39.pyc
│  │     │  │     ├─ wheel_builder.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ file_cache.cpython-39.pyc
│  │     │  │  │  │     ├─ redis_cache.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ adapter.cpython-39.pyc
│  │     │  │  │     ├─ cache.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ controller.cpython-39.pyc
│  │     │  │  │     ├─ filewrapper.cpython-39.pyc
│  │     │  │  │     ├─ heuristics.cpython-39.pyc
│  │     │  │  │     ├─ serialize.cpython-39.pyc
│  │     │  │  │     ├─ wrapper.cpython-39.pyc
│  │     │  │  │     ├─ _cmd.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ chardet
│  │     │  │  │  ├─ big5freq.py
│  │     │  │  │  ├─ big5prober.py
│  │     │  │  │  ├─ chardistribution.py
│  │     │  │  │  ├─ charsetgroupprober.py
│  │     │  │  │  ├─ charsetprober.py
│  │     │  │  │  ├─ cli
│  │     │  │  │  │  ├─ chardetect.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ chardetect.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ codingstatemachine.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cp949prober.py
│  │     │  │  │  ├─ enums.py
│  │     │  │  │  ├─ escprober.py
│  │     │  │  │  ├─ escsm.py
│  │     │  │  │  ├─ eucjpprober.py
│  │     │  │  │  ├─ euckrfreq.py
│  │     │  │  │  ├─ euckrprober.py
│  │     │  │  │  ├─ euctwfreq.py
│  │     │  │  │  ├─ euctwprober.py
│  │     │  │  │  ├─ gb2312freq.py
│  │     │  │  │  ├─ gb2312prober.py
│  │     │  │  │  ├─ hebrewprober.py
│  │     │  │  │  ├─ jisfreq.py
│  │     │  │  │  ├─ jpcntx.py
│  │     │  │  │  ├─ langbulgarianmodel.py
│  │     │  │  │  ├─ langgreekmodel.py
│  │     │  │  │  ├─ langhebrewmodel.py
│  │     │  │  │  ├─ langhungarianmodel.py
│  │     │  │  │  ├─ langrussianmodel.py
│  │     │  │  │  ├─ langthaimodel.py
│  │     │  │  │  ├─ langturkishmodel.py
│  │     │  │  │  ├─ latin1prober.py
│  │     │  │  │  ├─ mbcharsetprober.py
│  │     │  │  │  ├─ mbcsgroupprober.py
│  │     │  │  │  ├─ mbcssm.py
│  │     │  │  │  ├─ metadata
│  │     │  │  │  │  ├─ languages.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ languages.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ sbcharsetprober.py
│  │     │  │  │  ├─ sbcsgroupprober.py
│  │     │  │  │  ├─ sjisprober.py
│  │     │  │  │  ├─ universaldetector.py
│  │     │  │  │  ├─ utf8prober.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ big5freq.cpython-39.pyc
│  │     │  │  │     ├─ big5prober.cpython-39.pyc
│  │     │  │  │     ├─ chardistribution.cpython-39.pyc
│  │     │  │  │     ├─ charsetgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ charsetprober.cpython-39.pyc
│  │     │  │  │     ├─ codingstatemachine.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ cp949prober.cpython-39.pyc
│  │     │  │  │     ├─ enums.cpython-39.pyc
│  │     │  │  │     ├─ escprober.cpython-39.pyc
│  │     │  │  │     ├─ escsm.cpython-39.pyc
│  │     │  │  │     ├─ eucjpprober.cpython-39.pyc
│  │     │  │  │     ├─ euckrfreq.cpython-39.pyc
│  │     │  │  │     ├─ euckrprober.cpython-39.pyc
│  │     │  │  │     ├─ euctwfreq.cpython-39.pyc
│  │     │  │  │     ├─ euctwprober.cpython-39.pyc
│  │     │  │  │     ├─ gb2312freq.cpython-39.pyc
│  │     │  │  │     ├─ gb2312prober.cpython-39.pyc
│  │     │  │  │     ├─ hebrewprober.cpython-39.pyc
│  │     │  │  │     ├─ jisfreq.cpython-39.pyc
│  │     │  │  │     ├─ jpcntx.cpython-39.pyc
│  │     │  │  │     ├─ langbulgarianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langgreekmodel.cpython-39.pyc
│  │     │  │  │     ├─ langhebrewmodel.cpython-39.pyc
│  │     │  │  │     ├─ langhungarianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langrussianmodel.cpython-39.pyc
│  │     │  │  │     ├─ langthaimodel.cpython-39.pyc
│  │     │  │  │     ├─ langturkishmodel.cpython-39.pyc
│  │     │  │  │     ├─ latin1prober.cpython-39.pyc
│  │     │  │  │     ├─ mbcharsetprober.cpython-39.pyc
│  │     │  │  │     ├─ mbcsgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ mbcssm.cpython-39.pyc
│  │     │  │  │     ├─ sbcharsetprober.cpython-39.pyc
│  │     │  │  │     ├─ sbcsgroupprober.cpython-39.pyc
│  │     │  │  │     ├─ sjisprober.cpython-39.pyc
│  │     │  │  │     ├─ universaldetector.cpython-39.pyc
│  │     │  │  │     ├─ utf8prober.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ colorama
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ ansitowin32.py
│  │     │  │  │  ├─ initialise.py
│  │     │  │  │  ├─ win32.py
│  │     │  │  │  ├─ winterm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ansi.cpython-39.pyc
│  │     │  │  │     ├─ ansitowin32.cpython-39.pyc
│  │     │  │  │     ├─ initialise.cpython-39.pyc
│  │     │  │  │     ├─ win32.cpython-39.pyc
│  │     │  │  │     ├─ winterm.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _backport
│  │     │  │  │  │  ├─ misc.py
│  │     │  │  │  │  ├─ shutil.py
│  │     │  │  │  │  ├─ sysconfig.cfg
│  │     │  │  │  │  ├─ sysconfig.py
│  │     │  │  │  │  ├─ tarfile.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ misc.cpython-39.pyc
│  │     │  │  │  │     ├─ shutil.cpython-39.pyc
│  │     │  │  │  │     ├─ sysconfig.cpython-39.pyc
│  │     │  │  │  │     ├─ tarfile.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ database.cpython-39.pyc
│  │     │  │  │     ├─ index.cpython-39.pyc
│  │     │  │  │     ├─ locators.cpython-39.pyc
│  │     │  │  │     ├─ manifest.cpython-39.pyc
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ metadata.cpython-39.pyc
│  │     │  │  │     ├─ resources.cpython-39.pyc
│  │     │  │  │     ├─ scripts.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ wheel.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ distro.py
│  │     │  │  ├─ html5lib
│  │     │  │  │  ├─ constants.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ alphabeticalattributes.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ inject_meta_charset.py
│  │     │  │  │  │  ├─ lint.py
│  │     │  │  │  │  ├─ optionaltags.py
│  │     │  │  │  │  ├─ sanitizer.py
│  │     │  │  │  │  ├─ whitespace.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ alphabeticalattributes.cpython-39.pyc
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ inject_meta_charset.cpython-39.pyc
│  │     │  │  │  │     ├─ lint.cpython-39.pyc
│  │     │  │  │  │     ├─ optionaltags.cpython-39.pyc
│  │     │  │  │  │     ├─ sanitizer.cpython-39.pyc
│  │     │  │  │  │     ├─ whitespace.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ html5parser.py
│  │     │  │  │  ├─ serializer.py
│  │     │  │  │  ├─ treeadapters
│  │     │  │  │  │  ├─ genshi.py
│  │     │  │  │  │  ├─ sax.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ genshi.cpython-39.pyc
│  │     │  │  │  │     ├─ sax.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ treebuilders
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ dom.py
│  │     │  │  │  │  ├─ etree.py
│  │     │  │  │  │  ├─ etree_lxml.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ dom.cpython-39.pyc
│  │     │  │  │  │     ├─ etree.cpython-39.pyc
│  │     │  │  │  │     ├─ etree_lxml.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ treewalkers
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ dom.py
│  │     │  │  │  │  ├─ etree.py
│  │     │  │  │  │  ├─ etree_lxml.py
│  │     │  │  │  │  ├─ genshi.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-39.pyc
│  │     │  │  │  │     ├─ dom.cpython-39.pyc
│  │     │  │  │  │     ├─ etree.cpython-39.pyc
│  │     │  │  │  │     ├─ etree_lxml.cpython-39.pyc
│  │     │  │  │  │     ├─ genshi.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _ihatexml.py
│  │     │  │  │  ├─ _inputstream.py
│  │     │  │  │  ├─ _tokenizer.py
│  │     │  │  │  ├─ _trie
│  │     │  │  │  │  ├─ py.py
│  │     │  │  │  │  ├─ _base.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ py.cpython-39.pyc
│  │     │  │  │  │     ├─ _base.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constants.cpython-39.pyc
│  │     │  │  │     ├─ html5parser.cpython-39.pyc
│  │     │  │  │     ├─ serializer.cpython-39.pyc
│  │     │  │  │     ├─ _ihatexml.cpython-39.pyc
│  │     │  │  │     ├─ _inputstream.cpython-39.pyc
│  │     │  │  │     ├─ _tokenizer.cpython-39.pyc
│  │     │  │  │     ├─ _utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ codec.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ idnadata.cpython-39.pyc
│  │     │  │  │     ├─ intranges.cpython-39.pyc
│  │     │  │  │     ├─ package_data.cpython-39.pyc
│  │     │  │  │     ├─ uts46data.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │  │     ├─ ext.cpython-39.pyc
│  │     │  │  │     ├─ fallback.cpython-39.pyc
│  │     │  │  │     ├─ _version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _manylinux.cpython-39.pyc
│  │     │  │  │     ├─ _musllinux.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pep517
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ colorlog.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ dirtools.py
│  │     │  │  │  ├─ envbuild.py
│  │     │  │  │  ├─ in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _in_process.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ meta.py
│  │     │  │  │  ├─ wrappers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ build.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ colorlog.cpython-39.pyc
│  │     │  │  │     ├─ compat.cpython-39.pyc
│  │     │  │  │     ├─ dirtools.cpython-39.pyc
│  │     │  │  │     ├─ envbuild.cpython-39.pyc
│  │     │  │  │     ├─ meta.cpython-39.pyc
│  │     │  │  │     ├─ wrappers.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ py31compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ py31compat.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ platformdirs
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ android.cpython-39.pyc
│  │     │  │  │     ├─ api.cpython-39.pyc
│  │     │  │  │     ├─ macos.cpython-39.pyc
│  │     │  │  │     ├─ unix.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ windows.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ progress
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ colors.py
│  │     │  │  │  ├─ counter.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bar.cpython-39.pyc
│  │     │  │  │     ├─ colors.cpython-39.pyc
│  │     │  │  │     ├─ counter.cpython-39.pyc
│  │     │  │  │     ├─ spinner.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pygments
│  │     │  │  │  ├─ cmdline.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ formatters
│  │     │  │  │  │  ├─ bbcode.py
│  │     │  │  │  │  ├─ groff.py
│  │     │  │  │  │  ├─ html.py
│  │     │  │  │  │  ├─ img.py
│  │     │  │  │  │  ├─ irc.py
│  │     │  │  │  │  ├─ latex.py
│  │     │  │  │  │  ├─ other.py
│  │     │  │  │  │  ├─ pangomarkup.py
│  │     │  │  │  │  ├─ rtf.py
│  │     │  │  │  │  ├─ svg.py
│  │     │  │  │  │  ├─ terminal.py
│  │     │  │  │  │  ├─ terminal256.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ bbcode.cpython-39.pyc
│  │     │  │  │  │     ├─ groff.cpython-39.pyc
│  │     │  │  │  │     ├─ html.cpython-39.pyc
│  │     │  │  │  │     ├─ img.cpython-39.pyc
│  │     │  │  │  │     ├─ irc.cpython-39.pyc
│  │     │  │  │  │     ├─ latex.cpython-39.pyc
│  │     │  │  │  │     ├─ other.cpython-39.pyc
│  │     │  │  │  │     ├─ pangomarkup.cpython-39.pyc
│  │     │  │  │  │     ├─ rtf.cpython-39.pyc
│  │     │  │  │  │     ├─ svg.cpython-39.pyc
│  │     │  │  │  │     ├─ terminal.cpython-39.pyc
│  │     │  │  │  │     ├─ terminal256.cpython-39.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ lexers
│  │     │  │  │  │  ├─ python.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ python.cpython-39.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styles
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmdline.cpython-39.pyc
│  │     │  │  │     ├─ console.cpython-39.pyc
│  │     │  │  │     ├─ filter.cpython-39.pyc
│  │     │  │  │     ├─ formatter.cpython-39.pyc
│  │     │  │  │     ├─ lexer.cpython-39.pyc
│  │     │  │  │     ├─ modeline.cpython-39.pyc
│  │     │  │  │     ├─ plugin.cpython-39.pyc
│  │     │  │  │     ├─ regexopt.cpython-39.pyc
│  │     │  │  │     ├─ scanner.cpython-39.pyc
│  │     │  │  │     ├─ sphinxext.cpython-39.pyc
│  │     │  │  │     ├─ style.cpython-39.pyc
│  │     │  │  │     ├─ token.cpython-39.pyc
│  │     │  │  │     ├─ unistring.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-39.pyc
│  │     │  │  │     ├─ common.cpython-39.pyc
│  │     │  │  │     ├─ core.cpython-39.pyc
│  │     │  │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │  │     ├─ helpers.cpython-39.pyc
│  │     │  │  │     ├─ results.cpython-39.pyc
│  │     │  │  │     ├─ testing.cpython-39.pyc
│  │     │  │  │     ├─ unicode.cpython-39.pyc
│  │     │  │  │     ├─ util.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __pycache__
│  │     │  │  │  │  ├─ adapters.cpython-39.pyc
│  │     │  │  │  │  ├─ api.cpython-39.pyc
│  │     │  │  │  │  ├─ auth.cpython-39.pyc
│  │     │  │  │  │  ├─ certs.cpython-39.pyc
│  │     │  │  │  │  ├─ compat.cpython-39.pyc
│  │     │  │  │  │  ├─ cookies.cpython-39.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-39.pyc
│  │     │  │  │  │  ├─ help.cpython-39.pyc
│  │     │  │  │  │  ├─ models.cpython-39.pyc
│  │     │  │  │  │  ├─ packages.cpython-39.pyc
│  │     │  │  │  │  ├─ sessions.cpython-39.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-39.pyc
│  │     │  │  │  │  ├─ structures.cpython-39.pyc
│  │     │  │  │  │  ├─ utils.cpython-39.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.cpython-39.pyc
│  │     │  │  │  │  └─ __version__.cpython-39.pyc
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ compat
│  │     │  │  │  │  ├─ collections_abc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ collections_abc.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ providers.cpython-39.pyc
│  │     │  │  │     ├─ reporters.cpython-39.pyc
│  │     │  │  │     ├─ resolvers.cpython-39.pyc
│  │     │  │  │     ├─ structs.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ rich
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ tabulate.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  ├─ tree.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _lru_cache.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-39.pyc
│  │     │  │  │     ├─ align.cpython-39.pyc
│  │     │  │  │     ├─ ansi.cpython-39.pyc
│  │     │  │  │     ├─ bar.cpython-39.pyc
│  │     │  │  │     ├─ box.cpython-39.pyc
│  │     │  │  │     ├─ cells.cpython-39.pyc
│  │     │  │  │     ├─ color.cpython-39.pyc
│  │     │  │  │     ├─ color_triplet.cpython-39.pyc
│  │     │  │  │     ├─ columns.cpython-39.pyc
│  │     │  │  │     ├─ console.cpython-39.pyc
│  │     │  │  │     ├─ constrain.cpython-39.pyc
│  │     │  │  │     ├─ containers.cpython-39.pyc
│  │     │  │  │     ├─ control.cpython-39.pyc
│  │     │  │  │     ├─ default_styles.cpython-39.pyc
│  │     │  │  │     ├─ diagnose.cpython-39.pyc
│  │     │  │  │     ├─ emoji.cpython-39.pyc
│  │     │  │  │     ├─ errors.cpython-39.pyc
│  │     │  │  │     ├─ filesize.cpython-39.pyc
│  │     │  │  │     ├─ file_proxy.cpython-39.pyc
│  │     │  │  │     ├─ highlighter.cpython-39.pyc
│  │     │  │  │     ├─ json.cpython-39.pyc
│  │     │  │  │     ├─ jupyter.cpython-39.pyc
│  │     │  │  │     ├─ layout.cpython-39.pyc
│  │     │  │  │     ├─ live.cpython-39.pyc
│  │     │  │  │     ├─ live_render.cpython-39.pyc
│  │     │  │  │     ├─ logging.cpython-39.pyc
│  │     │  │  │     ├─ markup.cpython-39.pyc
│  │     │  │  │     ├─ measure.cpython-39.pyc
│  │     │  │  │     ├─ padding.cpython-39.pyc
│  │     │  │  │     ├─ pager.cpython-39.pyc
│  │     │  │  │     ├─ palette.cpython-39.pyc
│  │     │  │  │     ├─ panel.cpython-39.pyc
│  │     │  │  │     ├─ pretty.cpython-39.pyc
│  │     │  │  │     ├─ progress.cpython-39.pyc
│  │     │  │  │     ├─ progress_bar.cpython-39.pyc
│  │     │  │  │     ├─ prompt.cpython-39.pyc
│  │     │  │  │     ├─ protocol.cpython-39.pyc
│  │     │  │  │     ├─ region.cpython-39.pyc
│  │     │  │  │     ├─ repr.cpython-39.pyc
│  │     │  │  │     ├─ rule.cpython-39.pyc
│  │     │  │  │     ├─ scope.cpython-39.pyc
│  │     │  │  │     ├─ screen.cpython-39.pyc
│  │     │  │  │     ├─ segment.cpython-39.pyc
│  │     │  │  │     ├─ spinner.cpython-39.pyc
│  │     │  │  │     ├─ status.cpython-39.pyc
│  │     │  │  │     ├─ style.cpython-39.pyc
│  │     │  │  │     ├─ styled.cpython-39.pyc
│  │     │  │  │     ├─ syntax.cpython-39.pyc
│  │     │  │  │     ├─ table.cpython-39.pyc
│  │     │  │  │     ├─ tabulate.cpython-39.pyc
│  │     │  │  │     ├─ terminal_theme.cpython-39.pyc
│  │     │  │  │     ├─ text.cpython-39.pyc
│  │     │  │  │     ├─ theme.cpython-39.pyc
│  │     │  │  │     ├─ themes.cpython-39.pyc
│  │     │  │  │     ├─ traceback.cpython-39.pyc
│  │     │  │  │     ├─ tree.cpython-39.pyc
│  │     │  │  │     ├─ _cell_widths.cpython-39.pyc
│  │     │  │  │     ├─ _emoji_codes.cpython-39.pyc
│  │     │  │  │     ├─ _emoji_replace.cpython-39.pyc
│  │     │  │  │     ├─ _extension.cpython-39.pyc
│  │     │  │  │     ├─ _inspect.cpython-39.pyc
│  │     │  │  │     ├─ _log_render.cpython-39.pyc
│  │     │  │  │     ├─ _loop.cpython-39.pyc
│  │     │  │  │     ├─ _lru_cache.cpython-39.pyc
│  │     │  │  │     ├─ _palettes.cpython-39.pyc
│  │     │  │  │     ├─ _pick.cpython-39.pyc
│  │     │  │  │     ├─ _ratio.cpython-39.pyc
│  │     │  │  │     ├─ _spinners.cpython-39.pyc
│  │     │  │  │     ├─ _stack.cpython-39.pyc
│  │     │  │  │     ├─ _timer.cpython-39.pyc
│  │     │  │  │     ├─ _windows.cpython-39.pyc
│  │     │  │  │     ├─ _wrap.cpython-39.pyc
│  │     │  │  │     ├─ __init__.cpython-39.pyc
│  │     │  │  │     └─ __main__.cpython-39.pyc
│  │     │  │  ├─ six.py
│  │     │  │  ├─ tenacity
│  │     │  │  │  ├─ after.py
│  │     │  │  │  ├─ before.py
│  │     │  │  │  ├─ before_sleep.py
│  │     │  │  │  ├─ nap.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ stop.py
│  │     │  │  │  ├─ tornadoweb.py
│  │     │  │  │  ├─ wait.py
│  │     │  │  │  ├─ _asyncio.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ after.cpython-39.pyc
│  │     │  │  │     ├─ before.cpython-39.pyc
│  │     │  │  │     ├─ before_sleep.cpython-39.pyc
│  │     │  │  │     ├─ nap.cpython-39.pyc
│  │     │  │  │     ├─ retry.cpython-39.pyc
│  │     │  │  │     ├─ stop.cpython-39.pyc
│  │     │  │  │     ├─ tornadoweb.cpython-39.pyc
│  │     │  │  │     ├─ wait.cpython-39.pyc
│  │     │  │  │     ├─ _asyncio.cpython-39.pyc
│  │     │  │  │     ├─ _utils.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-39.pyc
│  │     │  │  │     ├─ _re.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ _securetransport
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  ├─ low_level.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ bindings.cpython-39.pyc
│  │     │  │  │  │  │     ├─ low_level.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ appengine.cpython-39.pyc
│  │     │  │  │  │     ├─ ntlmpool.cpython-39.pyc
│  │     │  │  │  │     ├─ pyopenssl.cpython-39.pyc
│  │     │  │  │  │     ├─ securetransport.cpython-39.pyc
│  │     │  │  │  │     ├─ socks.cpython-39.pyc
│  │     │  │  │  │     ├─ _appengine_environ.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ packages
│  │     │  │  │  │  ├─ backports
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ makefile.cpython-39.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  │  ├─ six.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ six.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ connection.cpython-39.pyc
│  │     │  │  │  │     ├─ proxy.cpython-39.pyc
│  │     │  │  │  │     ├─ queue.cpython-39.pyc
│  │     │  │  │  │     ├─ request.cpython-39.pyc
│  │     │  │  │  │     ├─ response.cpython-39.pyc
│  │     │  │  │  │     ├─ retry.cpython-39.pyc
│  │     │  │  │  │     ├─ ssltransport.cpython-39.pyc
│  │     │  │  │  │     ├─ ssl_.cpython-39.pyc
│  │     │  │  │  │     ├─ ssl_match_hostname.cpython-39.pyc
│  │     │  │  │  │     ├─ timeout.cpython-39.pyc
│  │     │  │  │  │     ├─ url.cpython-39.pyc
│  │     │  │  │  │     ├─ wait.cpython-39.pyc
│  │     │  │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-39.pyc
│  │     │  │  │     ├─ connectionpool.cpython-39.pyc
│  │     │  │  │     ├─ exceptions.cpython-39.pyc
│  │     │  │  │     ├─ fields.cpython-39.pyc
│  │     │  │  │     ├─ filepost.cpython-39.pyc
│  │     │  │  │     ├─ poolmanager.cpython-39.pyc
│  │     │  │  │     ├─ request.cpython-39.pyc
│  │     │  │  │     ├─ response.cpython-39.pyc
│  │     │  │  │     ├─ _collections.cpython-39.pyc
│  │     │  │  │     ├─ _version.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ vendor.txt
│  │     │  │  ├─ webencodings
│  │     │  │  │  ├─ labels.py
│  │     │  │  │  ├─ mklabels.py
│  │     │  │  │  ├─ tests.py
│  │     │  │  │  ├─ x_user_defined.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ labels.cpython-39.pyc
│  │     │  │  │     ├─ mklabels.cpython-39.pyc
│  │     │  │  │     ├─ tests.cpython-39.pyc
│  │     │  │  │     ├─ x_user_defined.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ distro.cpython-39.pyc
│  │     │  │     ├─ six.cpython-39.pyc
│  │     │  │     ├─ typing_extensions.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ __init__.cpython-39.pyc
│  │     │     └─ __main__.cpython-39.pyc
│  │     ├─ pip-22.0.4.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pkg_resources
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ tests
│  │     │  │  └─ data
│  │     │  │     └─ my-test-package-source
│  │     │  │        ├─ setup.py
│  │     │  │        └─ __pycache__
│  │     │  │           └─ setup.cpython-39.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _typing.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _compat.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ _typing.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyparsing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-39.pyc
│  │     │  │     ├─ pyparsing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ setuptools
│  │     │  ├─ archive_util.py
│  │     │  ├─ build_meta.py
│  │     │  ├─ cli-32.exe
│  │     │  ├─ cli-64.exe
│  │     │  ├─ cli.exe
│  │     │  ├─ command
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ bdist_egg.py
│  │     │  │  ├─ bdist_rpm.py
│  │     │  │  ├─ build_clib.py
│  │     │  │  ├─ build_ext.py
│  │     │  │  ├─ build_py.py
│  │     │  │  ├─ develop.py
│  │     │  │  ├─ dist_info.py
│  │     │  │  ├─ easy_install.py
│  │     │  │  ├─ egg_info.py
│  │     │  │  ├─ install.py
│  │     │  │  ├─ install_egg_info.py
│  │     │  │  ├─ install_lib.py
│  │     │  │  ├─ install_scripts.py
│  │     │  │  ├─ launcher manifest.xml
│  │     │  │  ├─ py36compat.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ rotate.py
│  │     │  │  ├─ saveopts.py
│  │     │  │  ├─ sdist.py
│  │     │  │  ├─ setopt.py
│  │     │  │  ├─ test.py
│  │     │  │  ├─ upload.py
│  │     │  │  ├─ upload_docs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ alias.cpython-39.pyc
│  │     │  │     ├─ bdist_egg.cpython-39.pyc
│  │     │  │     ├─ bdist_rpm.cpython-39.pyc
│  │     │  │     ├─ build_clib.cpython-39.pyc
│  │     │  │     ├─ build_ext.cpython-39.pyc
│  │     │  │     ├─ build_py.cpython-39.pyc
│  │     │  │     ├─ develop.cpython-39.pyc
│  │     │  │     ├─ dist_info.cpython-39.pyc
│  │     │  │     ├─ easy_install.cpython-39.pyc
│  │     │  │     ├─ egg_info.cpython-39.pyc
│  │     │  │     ├─ install.cpython-39.pyc
│  │     │  │     ├─ install_egg_info.cpython-39.pyc
│  │     │  │     ├─ install_lib.cpython-39.pyc
│  │     │  │     ├─ install_scripts.cpython-39.pyc
│  │     │  │     ├─ py36compat.cpython-39.pyc
│  │     │  │     ├─ register.cpython-39.pyc
│  │     │  │     ├─ rotate.cpython-39.pyc
│  │     │  │     ├─ saveopts.cpython-39.pyc
│  │     │  │     ├─ sdist.cpython-39.pyc
│  │     │  │     ├─ setopt.cpython-39.pyc
│  │     │  │     ├─ test.cpython-39.pyc
│  │     │  │     ├─ upload.cpython-39.pyc
│  │     │  │     ├─ upload_docs.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ config.py
│  │     │  ├─ depends.py
│  │     │  ├─ dep_util.py
│  │     │  ├─ dist.py
│  │     │  ├─ errors.py
│  │     │  ├─ extension.py
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ glob.py
│  │     │  ├─ gui-32.exe
│  │     │  ├─ gui-64.exe
│  │     │  ├─ gui.exe
│  │     │  ├─ installer.py
│  │     │  ├─ launch.py
│  │     │  ├─ monkey.py
│  │     │  ├─ msvc.py
│  │     │  ├─ namespaces.py
│  │     │  ├─ package_index.py
│  │     │  ├─ py34compat.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ script (dev).tmpl
│  │     │  ├─ script.tmpl
│  │     │  ├─ unicode_utils.py
│  │     │  ├─ version.py
│  │     │  ├─ wheel.py
│  │     │  ├─ windows_support.py
│  │     │  ├─ _deprecation_warning.py
│  │     │  ├─ _distutils
│  │     │  │  ├─ archive_util.py
│  │     │  │  ├─ bcppcompiler.py
│  │     │  │  ├─ ccompiler.py
│  │     │  │  ├─ cmd.py
│  │     │  │  ├─ command
│  │     │  │  │  ├─ bdist.py
│  │     │  │  │  ├─ bdist_dumb.py
│  │     │  │  │  ├─ bdist_msi.py
│  │     │  │  │  ├─ bdist_rpm.py
│  │     │  │  │  ├─ bdist_wininst.py
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ build_clib.py
│  │     │  │  │  ├─ build_ext.py
│  │     │  │  │  ├─ build_py.py
│  │     │  │  │  ├─ build_scripts.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ clean.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ install_data.py
│  │     │  │  │  ├─ install_egg_info.py
│  │     │  │  │  ├─ install_headers.py
│  │     │  │  │  ├─ install_lib.py
│  │     │  │  │  ├─ install_scripts.py
│  │     │  │  │  ├─ py37compat.py
│  │     │  │  │  ├─ register.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ upload.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bdist.cpython-39.pyc
│  │     │  │  │     ├─ bdist_dumb.cpython-39.pyc
│  │     │  │  │     ├─ bdist_msi.cpython-39.pyc
│  │     │  │  │     ├─ bdist_rpm.cpython-39.pyc
│  │     │  │  │     ├─ bdist_wininst.cpython-39.pyc
│  │     │  │  │     ├─ build.cpython-39.pyc
│  │     │  │  │     ├─ build_clib.cpython-39.pyc
│  │     │  │  │     ├─ build_ext.cpython-39.pyc
│  │     │  │  │     ├─ build_py.cpython-39.pyc
│  │     │  │  │     ├─ build_scripts.cpython-39.pyc
│  │     │  │  │     ├─ check.cpython-39.pyc
│  │     │  │  │     ├─ clean.cpython-39.pyc
│  │     │  │  │     ├─ config.cpython-39.pyc
│  │     │  │  │     ├─ install.cpython-39.pyc
│  │     │  │  │     ├─ install_data.cpython-39.pyc
│  │     │  │  │     ├─ install_egg_info.cpython-39.pyc
│  │     │  │  │     ├─ install_headers.cpython-39.pyc
│  │     │  │  │     ├─ install_lib.cpython-39.pyc
│  │     │  │  │     ├─ install_scripts.cpython-39.pyc
│  │     │  │  │     ├─ py37compat.cpython-39.pyc
│  │     │  │  │     ├─ register.cpython-39.pyc
│  │     │  │  │     ├─ sdist.cpython-39.pyc
│  │     │  │  │     ├─ upload.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ config.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ cygwinccompiler.py
│  │     │  │  ├─ debug.py
│  │     │  │  ├─ dep_util.py
│  │     │  │  ├─ dir_util.py
│  │     │  │  ├─ dist.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ extension.py
│  │     │  │  ├─ fancy_getopt.py
│  │     │  │  ├─ filelist.py
│  │     │  │  ├─ file_util.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ msvc9compiler.py
│  │     │  │  ├─ msvccompiler.py
│  │     │  │  ├─ py35compat.py
│  │     │  │  ├─ py38compat.py
│  │     │  │  ├─ spawn.py
│  │     │  │  ├─ sysconfig.py
│  │     │  │  ├─ text_file.py
│  │     │  │  ├─ unixccompiler.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ versionpredicate.py
│  │     │  │  ├─ _msvccompiler.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ archive_util.cpython-39.pyc
│  │     │  │     ├─ bcppcompiler.cpython-39.pyc
│  │     │  │     ├─ ccompiler.cpython-39.pyc
│  │     │  │     ├─ cmd.cpython-39.pyc
│  │     │  │     ├─ config.cpython-39.pyc
│  │     │  │     ├─ core.cpython-39.pyc
│  │     │  │     ├─ cygwinccompiler.cpython-39.pyc
│  │     │  │     ├─ debug.cpython-39.pyc
│  │     │  │     ├─ dep_util.cpython-39.pyc
│  │     │  │     ├─ dir_util.cpython-39.pyc
│  │     │  │     ├─ dist.cpython-39.pyc
│  │     │  │     ├─ errors.cpython-39.pyc
│  │     │  │     ├─ extension.cpython-39.pyc
│  │     │  │     ├─ fancy_getopt.cpython-39.pyc
│  │     │  │     ├─ filelist.cpython-39.pyc
│  │     │  │     ├─ file_util.cpython-39.pyc
│  │     │  │     ├─ log.cpython-39.pyc
│  │     │  │     ├─ msvc9compiler.cpython-39.pyc
│  │     │  │     ├─ msvccompiler.cpython-39.pyc
│  │     │  │     ├─ py35compat.cpython-39.pyc
│  │     │  │     ├─ py38compat.cpython-39.pyc
│  │     │  │     ├─ spawn.cpython-39.pyc
│  │     │  │     ├─ sysconfig.cpython-39.pyc
│  │     │  │     ├─ text_file.cpython-39.pyc
│  │     │  │     ├─ unixccompiler.cpython-39.pyc
│  │     │  │     ├─ util.cpython-39.pyc
│  │     │  │     ├─ version.cpython-39.pyc
│  │     │  │     ├─ versionpredicate.cpython-39.pyc
│  │     │  │     ├─ _msvccompiler.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ _imp.py
│  │     │  ├─ _vendor
│  │     │  │  ├─ more_itertools
│  │     │  │  │  ├─ more.py
│  │     │  │  │  ├─ recipes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ more.cpython-39.pyc
│  │     │  │  │     ├─ recipes.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ ordered_set.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _typing.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-39.pyc
│  │     │  │  │     ├─ requirements.cpython-39.pyc
│  │     │  │  │     ├─ specifiers.cpython-39.pyc
│  │     │  │  │     ├─ tags.cpython-39.pyc
│  │     │  │  │     ├─ utils.cpython-39.pyc
│  │     │  │  │     ├─ version.cpython-39.pyc
│  │     │  │  │     ├─ _compat.cpython-39.pyc
│  │     │  │  │     ├─ _structures.cpython-39.pyc
│  │     │  │  │     ├─ _typing.cpython-39.pyc
│  │     │  │  │     ├─ __about__.cpython-39.pyc
│  │     │  │  │     └─ __init__.cpython-39.pyc
│  │     │  │  ├─ pyparsing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ordered_set.cpython-39.pyc
│  │     │  │     ├─ pyparsing.cpython-39.pyc
│  │     │  │     └─ __init__.cpython-39.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ archive_util.cpython-39.pyc
│  │     │     ├─ build_meta.cpython-39.pyc
│  │     │     ├─ config.cpython-39.pyc
│  │     │     ├─ depends.cpython-39.pyc
│  │     │     ├─ dep_util.cpython-39.pyc
│  │     │     ├─ dist.cpython-39.pyc
│  │     │     ├─ errors.cpython-39.pyc
│  │     │     ├─ extension.cpython-39.pyc
│  │     │     ├─ glob.cpython-39.pyc
│  │     │     ├─ installer.cpython-39.pyc
│  │     │     ├─ launch.cpython-39.pyc
│  │     │     ├─ monkey.cpython-39.pyc
│  │     │     ├─ msvc.cpython-39.pyc
│  │     │     ├─ namespaces.cpython-39.pyc
│  │     │     ├─ package_index.cpython-39.pyc
│  │     │     ├─ py34compat.cpython-39.pyc
│  │     │     ├─ sandbox.cpython-39.pyc
│  │     │     ├─ unicode_utils.cpython-39.pyc
│  │     │     ├─ version.cpython-39.pyc
│  │     │     ├─ wheel.cpython-39.pyc
│  │     │     ├─ windows_support.cpython-39.pyc
│  │     │     ├─ _deprecation_warning.cpython-39.pyc
│  │     │     ├─ _imp.cpython-39.pyc
│  │     │     └─ __init__.cpython-39.pyc
│  │     ├─ setuptools-58.1.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     └─ _distutils_hack
│  │        ├─ override.py
│  │        ├─ __init__.py
│  │        └─ __pycache__
│  │           ├─ override.cpython-39.pyc
│  │           └─ __init__.cpython-39.pyc
│  ├─ pyvenv.cfg
│  ├─ README.md
│  ├─ requirements.txt
│  └─ Scripts
│     ├─ activate
│     ├─ activate.bat
│     ├─ Activate.ps1
│     ├─ deactivate.bat
│     ├─ pip.exe
│     ├─ pip3.9.exe
│     ├─ pip3.exe
│     ├─ python.exe
│     └─ pythonw.exe
├─ frontend
│  ├─ assets
│  │  ├─ img
│  │  └─ styles
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.js
│     ├─ App.test.js
│     ├─ components
│     │  ├─ button
│     │  ├─ card
│     │  ├─ checkbox
│     │  ├─ footer
│     │  ├─ header
│     │  ├─ modal
│     │  └─ text-field
│     ├─ containers
│     │  ├─ layouts
│     │  │  ├─ AuthLayout.js
│     │  │  └─ DefaultLayout.js
│     │  └─ views
│     │     ├─ Create
│     │     │  └─ index.js
│     │     ├─ Edit
│     │     │  └─ index.js
│     │     ├─ Home
│     │     │  └─ index.js
│     │     ├─ Login
│     │     │  └─ index.js
│     │     └─ Register
│     │        └─ index.js
│     ├─ contexts
│     ├─ index.css
│     ├─ index.js
│     ├─ logo.svg
│     ├─ reportWebVitals.js
│     ├─ router
│     │  └─ PublicRoutes.js
│     ├─ setupTests.js
│     └─ utils
├─ react-folder-structure
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.js
│     ├─ App.test.js
│     ├─ assets
│     │  └─ styles
│     │     ├─ animations.scss
│     │     ├─ buttons.scss
│     │     ├─ overrides.scss
│     │     ├─ styles.scss
│     │     └─ variables.scss
│     ├─ components
│     │  └─ LanguageSelect.js
│     ├─ containers
│     │  ├─ layouts
│     │  │  ├─ auth
│     │  │  │  ├─ layout-auth.js
│     │  │  │  └─ layout-auth.scss
│     │  │  ├─ dashboard
│     │  │  │  ├─ layout-dashboard.js
│     │  │  │  └─ layout-dashboard.scss
│     │  │  └─ public
│     │  │     ├─ Footer
│     │  │     │  ├─ index.js
│     │  │     │  └─ style.scss
│     │  │     ├─ Header
│     │  │     │  ├─ index.js
│     │  │     │  └─ style.scss
│     │  │     ├─ layout-public.js
│     │  │     └─ layout-public.scss
│     │  └─ views
│     │     ├─ auth
│     │     │  ├─ ForgotPassword
│     │     │  │  ├─ index.js
│     │     │  │  └─ index.scss
│     │     │  ├─ Login
│     │     │  │  ├─ index.js
│     │     │  │  └─ index.scss
│     │     │  └─ Register
│     │     │     ├─ index.js
│     │     │     └─ index.scss
│     │     ├─ dashboard
│     │     │  ├─ Messages
│     │     │  │  ├─ index.js
│     │     │  │  └─ index.scss
│     │     │  ├─ Profile
│     │     │  │  ├─ index.js
│     │     │  │  └─ index.scss
│     │     │  └─ Settings
│     │     │     ├─ index.js
│     │     │     └─ index.scss
│     │     └─ public
│     │        ├─ About
│     │        │  ├─ index.js
│     │        │  └─ index.scss
│     │        ├─ Contact
│     │        │  ├─ index.js
│     │        │  └─ index.scss
│     │        ├─ Home
│     │        │  ├─ index.js
│     │        │  └─ index.scss
│     │        └─ NotFound
│     │           ├─ index.js
│     │           └─ index.scss
│     ├─ index.css
│     ├─ index.js
│     ├─ logo.svg
│     ├─ reportWebVitals.js
│     ├─ router
│     │  ├─ history.js
│     │  ├─ Navigation.js
│     │  └─ ProtectedRoute.js
│     └─ setupTests.js
└─ README.md

```