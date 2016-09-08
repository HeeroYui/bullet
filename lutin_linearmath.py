#!/usr/bin/python
# --------------------------------------------------------
# -- Linear Math librairy
# --------------------------------------------------------
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "Bullet lib linar Mathematic interface"

def get_licence():
	return "zlib"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "bullet-physics"

def get_maintainer():
	return ["Erwin Coumans <erwin.coumans@gmail.com>"]

def get_version():
	return [2,82,"r2704"]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
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
		'bullet-physics/src/LinearMath/btConvexHullComputer.cpp'
		])
	my_module.add_flag('c++', [
		'-Wno-write-strings',
		'-DHAVE_CONFIG_H',
		'-O2'])
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "bullet-physics/src"))
	my_module.add_header_file([
		'bullet-physics/src/LinearMath/btStackAlloc.h',
		'bullet-physics/src/LinearMath/btAlignedObjectArray.h',
		'bullet-physics/src/LinearMath/btScalar.h',
		'bullet-physics/src/LinearMath/btQuickprof.h',
		'bullet-physics/src/LinearMath/btMatrix3x3.h',
		'bullet-physics/src/LinearMath/btIDebugDraw.h',
		'bullet-physics/src/LinearMath/btPoolAllocator.h',
		'bullet-physics/src/LinearMath/btPolarDecomposition.h',
		'bullet-physics/src/LinearMath/btHashMap.h',
		'bullet-physics/src/LinearMath/btRandom.h',
		'bullet-physics/src/LinearMath/btMatrixX.h',
		'bullet-physics/src/LinearMath/btAabbUtil2.h',
		'bullet-physics/src/LinearMath/btMinMax.h',
		'bullet-physics/src/LinearMath/btDefaultMotionState.h',
		'bullet-physics/src/LinearMath/btVector3.h',
		'bullet-physics/src/LinearMath/btConvexHull.h',
		'bullet-physics/src/LinearMath/btMotionState.h',
		'bullet-physics/src/LinearMath/btAlignedAllocator.h',
		'bullet-physics/src/LinearMath/btTransformUtil.h',
		'bullet-physics/src/LinearMath/btGeometryUtil.h',
		'bullet-physics/src/LinearMath/btQuadWord.h',
		'bullet-physics/src/LinearMath/btQuaternion.h',
		'bullet-physics/src/LinearMath/btList.h',
		'bullet-physics/src/LinearMath/btGrahamScan2dConvexHull.h',
		'bullet-physics/src/LinearMath/btConvexHullComputer.h',
		'bullet-physics/src/LinearMath/btSerializer.h',
		'bullet-physics/src/LinearMath/btTransform.h'
		],
		destination_path="LinearMath")
	# depend on the cxx library (need <new> and somes things ...)
	my_module.add_depend([
	    'cxx',
	    'm'
	    ])
	return my_module






