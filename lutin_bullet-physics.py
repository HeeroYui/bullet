#!/usr/bin/python
# --------------------------------------------------------
# -- Bullet librairy
# --------------------------------------------------------
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "C++ physic engine"

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
	my_module.add_depend(['linearmath'])
	#remove compilation warning (specific for external libs):
	my_module.remove_compile_warning()
	my_module.add_flag('c++', [
	    '-Wno-write-strings',
	    '-DHAVE_CONFIG_H',
	    '-O2'])
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "bullet-physics/src/"), export=True)
	my_module.add_path(tools.get_current_path(__file__), export=True)
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "bullet-physics/Extras/ConvexDecomposition"))
	# lib BulletCollision
	my_module.add_src_file([
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btRaycastCallback.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btMinkowskiPenetrationDepthSolver.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btSubSimplexConvexCast.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btGjkEpaPenetrationDepthSolver.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btGjkConvexCast.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btPersistentManifold.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btConvexCast.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btPolyhedralContactClipping.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btContinuousConvexCollision.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btGjkPairDetector.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btGjkEpa2.cpp',
	    'bullet-physics/src/BulletCollision/NarrowPhaseCollision/btVoronoiSimplexSolver.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btCompoundCompoundCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btHashedSimplePairCache.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btActivatingCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btCollisionObject.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btEmptyCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btGhostObject.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btSphereSphereCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btSphereBoxCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btCollisionDispatcher.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btDefaultCollisionConfiguration.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btSimulationIslandManager.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btBoxBoxDetector.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btConvexPlaneCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btConvexConcaveCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btBoxBoxCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btBox2dBox2dCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/SphereTriangleDetector.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btManifoldResult.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btCollisionWorld.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btSphereTriangleCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btConvexConvexAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btConvex2dConvex2dAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btUnionFind.cpp',
	    'bullet-physics/src/BulletCollision/CollisionDispatch/btCompoundCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTetrahedronShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btShapeHull.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btMinkowskiSumShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btCompoundShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConeShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexPolyhedron.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btMultiSphereShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btUniformScalingShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btSphereShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleIndexVertexArray.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btBvhTriangleMeshShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleMeshShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleBuffer.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btStaticPlaneShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btPolyhedralConvexShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btEmptyShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btCollisionShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvex2dShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexInternalShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexHullShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleCallback.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btCapsuleShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexTriangleMeshShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConcaveShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btConvexPointCloudShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btBoxShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btBox2dShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btOptimizedBvh.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btHeightfieldTerrainShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btMultimaterialTriangleMeshShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btCylinderShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btScaledBvhTriangleMeshShape.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btStridingMeshInterface.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleIndexVertexMaterialArray.cpp',
	    'bullet-physics/src/BulletCollision/CollisionShapes/btTriangleMesh.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btAxisSweep3.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btOverlappingPairCache.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btDbvtBroadphase.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btMultiSapBroadphase.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btDispatcher.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btBroadphaseProxy.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btQuantizedBvh.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btDbvt.cpp',
	    'bullet-physics/src/BulletCollision/BroadphaseCollision/btSimpleBroadphase.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/btGImpactBvh.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/btGImpactQuantizedBvh.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/btTriangleShapeEx.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/btGImpactCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/btGImpactShape.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/gim_box_set.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/gim_contact.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/gim_memory.cpp',
	    'bullet-physics/src/BulletCollision/Gimpact/gim_tri_collision.cpp'])
	
	# lib BulletDynamics
	my_module.add_src_file([
	    'bullet-physics/src/BulletDynamics/Dynamics/btRigidBody.cpp',
	    'bullet-physics/src/BulletDynamics/Dynamics/btSimpleDynamicsWorld.cpp',
	    'bullet-physics/src/BulletDynamics/Dynamics/Bullet-C-API.cpp',
	    'bullet-physics/src/BulletDynamics/Dynamics/btDiscreteDynamicsWorld.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btGearConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btGeneric6DofConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btGeneric6DofSpringConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btSolve2LinearConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btPoint2PointConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btTypedConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btContactConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btSliderConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btConeTwistConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btHingeConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btHinge2Constraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btUniversalConstraint.cpp',
	    'bullet-physics/src/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolver.cpp',
	    'bullet-physics/src/BulletDynamics/Vehicle/btWheelInfo.cpp',
	    'bullet-physics/src/BulletDynamics/Vehicle/btRaycastVehicle.cpp',
	    'bullet-physics/src/BulletDynamics/Character/btKinematicCharacterController.cpp'])
	
	# lib BulletSoftBody
	my_module.add_src_file([
	    'bullet-physics/src/BulletSoftBody/btDefaultSoftBodySolver.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftBodyRigidBodyCollisionConfiguration.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftBody.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftRigidCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftBodyConcaveCollisionAlgorithm.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftRigidDynamicsWorld.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftBodyHelpers.cpp',
	    'bullet-physics/src/BulletSoftBody/btSoftSoftCollisionAlgorithm.cpp'])
	
	# lib gimpactutils
	my_module.add_src_file([
	    'bullet-physics/Extras/GIMPACTUtils/btGImpactConvexDecompositionShape.cpp'])
	
	
	# lib convexdecomposition
	my_module.add_src_file([
	    'bullet-physics/Extras/ConvexDecomposition/concavity.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/ConvexDecomposition.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/vlookup.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/bestfit.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/ConvexBuilder.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/cd_hull.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/raytri.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/splitplane.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/float_math.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/planetri.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/cd_wavefront.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/bestfitobb.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/meshvolume.cpp',
	    'bullet-physics/Extras/ConvexDecomposition/fitsphere.cpp'
		])
	
	
	"""
	# lib HACD
	my_module.add_src_file([
	    'bullet-physics/Extras/HACD/hacdGraph.cpp',
	    'bullet-physics/Extras/HACD/hacdHACD.cpp',
	    'bullet-physics/Extras/HACD/hacdICHull.cpp',
	    'bullet-physics/Extras/HACD/hacdManifoldMesh.cpp'])
	"""
	return my_module

