incdir = include_directories(['../include/gnuradio/howto','../include'])

howto_deps += [newsched_runtime_dep, volk_dep, fmt_dep, pmt_dep]
howto_sources += []

# This is ugly, and there HAS to be a better way to bring in dependencies
link_args = ['-lnewsched-pmt','-lnewsched-runtime']
block_cpp_args = ['-DHAVE_CPU']
if USE_CUDA
     block_cpp_args += '-DHAVE_CUDA'

    newsched_blocklib_howto_cu = library('newsched-blocklib-howto-cu', 
        howto_cu_sources, 
        include_directories : incdir, 
        install : true, 
        dependencies : [cuda_dep])

    newsched_blocklib_howto_cu_dep = declare_dependency(include_directories : incdir,
                        link_with : newsched_blocklib_howto_cu,
                        dependencies : cuda_dep)

    howto_deps += [cuda_dep, cusp_dep, newsched_blocklib_howto_cu_dep]
    link_args += '-lcusp'
endif

incdir = include_directories(['../include/gnuradio/howto','../include'])
newsched_blocklib_howto_lib = library('newsched-blocklib-howto', 
    howto_sources, 
    include_directories : incdir, 
    install : true,
    link_language: 'cpp',
    link_args : link_args,  # why is this necesary???
    dependencies : howto_deps,
    cpp_args : block_cpp_args)

newsched_blocklib_howto_dep = declare_dependency(include_directories : incdir,
					   link_with : newsched_blocklib_howto_lib,
                       dependencies : howto_deps)
