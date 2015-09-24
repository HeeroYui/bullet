#!/usr/bin/python
# --------------------------------------------------------
# -- Linear Math librairy
# --------------------------------------------------------
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Bullet lib linar Mathematic interface"


def create(target):
	my_module = module.Module(__file__, 'linearmath', 'LIBRARY')
	#remove compilation warning (specific for external libs):
	my_module.remove_compile_warning()
	
	my_module.add_src_file([
		'bullet-physics/src/LinearMath/btQuickprof.cpp',
		'bullet-physics/src/LinearMath/btGeometryUtil.cpp',
		'bullet-physics/src/LinearMath/btAlignedAllocator.cpp',
		'bullet-physics/src/LinearMath/btSerializer.cpp',
		'bullet-physics/src/LinearMath/btConvexHull.cpp',
		'bullet-physics/src/LinearMath/btPolarDecomposition.cpp',
		'bullet-physics/src/LinearMath/btVector3.cpp',
		'bullet-physics/src/LinearMath/btConvexHullComputer.cpp'])
	
	my_module.compile_flags('c', [
		'-Wno-write-strings',
		'-DHAVE_CONFIG_H',
		'-O2'])
	
	my_module.add_export_path(tools.get_current_path(__file__)+"/bullet-physics/src/")
	
	# add the currrent module at the 
	return my_module






