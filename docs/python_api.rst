Python API
----------

``Databuild`` can be integrated in your python project. Just import the ``build`` function::

    from databuild.builder import build

    build('buildfile.json')

Supported arguments:
    * ``build_file`` Required. Path to the :doc:`buildfile`.
    * ``settings`` Optional. Python module path containing the settings. Defaults to ``datbuild.settings``
    * ``echo`` Optional. Set this to ``True`` if you want the operations' description printed to the screen. Defaults to ``False``.
    

