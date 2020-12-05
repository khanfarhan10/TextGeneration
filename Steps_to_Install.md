Microsoft Windows [Version 10.0.18363.1198]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>python --version
Python 3.9.0

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>piprsi on
'piprsi' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>pip --version
pip 20.2.3 from c:\users\tannistha pal\appdata\local\programs\python\python39\lib\site-packages\pip (python 3.9)

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\tannistha pal\appdata\local\programs\python\python39\lib\site-packages (20.2.1)
Requirement already satisfied: filelock<4,>=3.0.0 in c:\users\tannistha pal\appdata\local\programs\python\python39\lib\site-packages (from virtualenv) (3.0.12)
Requirement already satisfied: appdirs<2,>=1.4.3 in c:\users\tannistha pal\appdata\local\programs\python\python39\lib\site-packages (from virtualenv) (1.4.4)
Requirement already satisfied: six<2,>=1.9.0 in c:\users\tannistha pal\appdata\roaming\python\python39\site-packages (from virtualenv) (1.15.0)
Requirement already satisfied: distlib<1,>=0.3.1 in c:\users\tannistha pal\appdata\local\programs\python\python39\lib\site-packages (from virtualenv) (0.3.1)
WARNING: You are using pip version 20.2.3; however, version 20.3 is available.
You should consider upgrading via the 'c:\users\tannistha pal\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>mkdir TextGenEnv

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>virtualenv TextGenEnv
created virtual environment CPython3.9.0.final.0-64 in 1217ms
  creator CPython3Windows(dest=C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Tannistha Pal\AppData\Local\pypa\virtualenv)
    added seed packages: pip==20.2.4, setuptools==50.3.2, wheel==0.35.1
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>TextGenEnv\Scripts\activate

(TextGenEnv) C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>pip install -r TextGenReq.txt
Collecting numpy==1.18.5
  Using cached numpy-1.18.5.zip (5.4 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... error
    ERROR: Command errored out with exit status 1:
     command: 'C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\Scripts\python.exe' 'C:\Users\Tannistha 
Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib\site-packages\pip\_vendor\pep517\_in_process.py' prepare_metadata_for_build_wheel 'C:\Users\TANNIS~1\AppData\Local\Temp\tmpsxd23ovb'
         cwd: C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy
    Complete output (187 lines):
    Running from numpy source directory.
    setup.py:461: UserWarning: Unrecognized setuptools command, proceeding with generating Cython sources and expanding templates
      run_build = parse_setuppy_commands()
    Processing numpy/random\_bounded_integers.pxd.in
    Processing numpy/random\mtrand.pyx
    Processing numpy/random\_bit_generator.pyx
    Processing numpy/random\_bounded_integers.pyx.in
    Processing numpy/random\_common.pyx
    Processing numpy/random\_generator.pyx
    Processing numpy/random\_mt19937.pyx
    Processing numpy/random\_pcg64.pyx
    Processing numpy/random\_philox.pyx
    Processing numpy/random\_sfc64.pyx
    Cythonizing sources
    blas_opt_info:
    blas_mkl_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries mkl_rt not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    blis_info:
      libraries blis not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_info:
      libraries openblas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
    get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
    customize GnuFCompiler
    Could not locate executable g77
    Could not locate executable f77
    customize IntelVisualFCompiler
    Could not locate executable ifort
    Could not locate executable ifl
    customize AbsoftFCompiler
    Could not locate executable f90
    customize CompaqVisualFCompiler
    Could not locate executable DF
    customize IntelItaniumVisualFCompiler
    Could not locate executable efl
    customize Gnu95FCompiler
    Could not locate executable gfortran
    Could not locate executable f95
    customize G95FCompiler
    Could not locate executable g95
    customize IntelEM64VisualFCompiler
    customize IntelEM64TFCompiler
    Could not locate executable efort
    Could not locate executable efc
    customize PGroupFlangCompiler
    Could not locate executable flang
    don't know how to compile Fortran code on platform 'nt'
      NOT AVAILABLE

    atlas_3_10_blas_threads_info:
    Setting PTATLAS=ATLAS
      libraries tatlas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_3_10_blas_info:
      libraries satlas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_blas_threads_info:
    Setting PTATLAS=ATLAS
      libraries ptf77blas,ptcblas,atlas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_blas_info:
      libraries f77blas,cblas,atlas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    accelerate_info:
      NOT AVAILABLE

    C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy\numpy\distutils\system_info.py:1896: UserWarning:
        Optimized (vendor) Blas libraries are not found.
        Falls back to netlib Blas library which has worse performance.
        A better performance should be easily gained by switching
        Blas library.
      if self._calc_info(blas):
    blas_info:
      libraries blas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy\numpy\distutils\system_info.py:1896: UserWarning:
        Blas (http://www.netlib.org/blas/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [blas]) or by setting
        the BLAS environment variable.
      if self._calc_info(blas):
    blas_src_info:
      NOT AVAILABLE

    C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy\numpy\distutils\system_info.py:1896: UserWarning:
        Blas (http://www.netlib.org/blas/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [blas_src]) or by setting
        the BLAS_SRC environment variable.
      if self._calc_info(blas):
      NOT AVAILABLE

    non-existing path in 'numpy\\distutils': 'site.cfg'
    lapack_opt_info:
    lapack_mkl_info:
      libraries mkl_rt not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_lapack_info:
      libraries openblas not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_clapack_info:
      libraries openblas,lapack not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    flame_info:
      libraries flame not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_3_10_threads_info:
    Setting PTATLAS=ATLAS
      libraries lapack_atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries tatlas,tatlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries lapack_atlas not found in C:\
      libraries tatlas,tatlas not found in C:\
    <class 'numpy.distutils.system_info.atlas_3_10_threads_info'>
      NOT AVAILABLE

    atlas_3_10_info:
      libraries lapack_atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries satlas,satlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries lapack_atlas not found in C:\
      libraries satlas,satlas not found in C:\
    <class 'numpy.distutils.system_info.atlas_3_10_info'>
      NOT AVAILABLE

    atlas_threads_info:
    Setting PTATLAS=ATLAS
      libraries lapack_atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries ptf77blas,ptcblas,atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries lapack_atlas not found in C:\
      libraries ptf77blas,ptcblas,atlas not found in C:\
    <class 'numpy.distutils.system_info.atlas_threads_info'>
      NOT AVAILABLE

    atlas_info:
      libraries lapack_atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib
      libraries f77blas,cblas,atlas not found in C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib   
      libraries lapack_atlas not found in C:\
      libraries f77blas,cblas,atlas not found in C:\
    <class 'numpy.distutils.system_info.atlas_info'>
      NOT AVAILABLE

    lapack_info:
      libraries lapack not found in ['C:\\Users\\Tannistha Pal\\Documents\\GitHub\\TextGeneration\\TextGenEnv\\lib', 'C:\\']
      NOT AVAILABLE

    C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy\numpy\distutils\system_info.py:1730: UserWarning:
        Lapack (http://www.netlib.org/lapack/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [lapack]) or by setting
        the LAPACK environment variable.
      return getattr(self, '_calc_info_{}'.format(name))()
    lapack_src_info:
      NOT AVAILABLE

    C:\Users\Tannistha Pal\AppData\Local\Temp\pip-install-uhgtam_a\numpy\numpy\distutils\system_info.py:1730: UserWarning:
        Lapack (http://www.netlib.org/lapack/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [lapack_src]) or by setting
        the LAPACK_SRC environment variable.
      return getattr(self, '_calc_info_{}'.format(name))()
      NOT AVAILABLE

    c:\users\tannistha pal\appdata\local\programs\python\python39\lib\distutils\dist.py:274: UserWarning: Unknown distribution option: 'define_macros'
      warnings.warn(msg)
    running dist_info
    running build_src
    build_src
    building py_modules sources
    creating build
    creating build\src.win-amd64-3.9
    creating build\src.win-amd64-3.9\numpy
    creating build\src.win-amd64-3.9\numpy\distutils
    building library "npymath" sources
    error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\Scripts\python.exe' 'C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\lib\site-packages\pip\_vendor\pep517\_in_process.py' prepare_metadata_for_build_wheel 'C:\Users\TANNIS~1\AppData\Local\Temp\tmpsxd23ovb' Check the logs for full command output.
WARNING: You are using pip version 20.2.4; however, version 20.3.1 is available.
You should consider upgrading via the 'C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration\TextGenEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(TextGenEnv) C:\Users\Tannistha Pal\Documents\GitHub\TextGeneration>