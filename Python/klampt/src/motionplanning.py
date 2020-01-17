# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""Python interface to C++ motion planing routines"""


from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_motionplanning', [dirname(__file__)])
        except ImportError:
            import _motionplanning
            return _motionplanning
        if fp is not None:
            try:
                _mod = imp.load_module('_motionplanning', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _motionplanning = swig_import_helper()
    del swig_import_helper
else:
    import _motionplanning
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _motionplanning.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _motionplanning.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _motionplanning.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _motionplanning.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _motionplanning.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _motionplanning.SwigPyIterator_equal(self, x)

    def copy(self):
        return _motionplanning.SwigPyIterator_copy(self)

    def next(self):
        return _motionplanning.SwigPyIterator_next(self)

    def __next__(self):
        return _motionplanning.SwigPyIterator___next__(self)

    def previous(self):
        return _motionplanning.SwigPyIterator_previous(self)

    def advance(self, n):
        return _motionplanning.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _motionplanning.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _motionplanning.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _motionplanning.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _motionplanning.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _motionplanning.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _motionplanning.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _motionplanning.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def setRandomSeed(seed):
    """
    setRandomSeed(int seed)



    Sets the random seed used by the configuration sampler.  

    """
    return _motionplanning.setRandomSeed(seed)

def setPlanJSONString(string):
    """
    setPlanJSONString(char const * string)



    Loads planner values from a JSON string.  

    """
    return _motionplanning.setPlanJSONString(string)

def getPlanJSONString():
    """
    getPlanJSONString() -> std::string



    Saves planner values to a JSON string.  

    """
    return _motionplanning.getPlanJSONString()

def setPlanType(type):
    """
    setPlanType(char const * type)



    Sets the planner type.  

    Valid values are  

    *   prm: the Probabilistic Roadmap algorithm  
    *   rrt: the Rapidly Exploring Random Trees algorithm  
    *   sbl: the Single-Query Bidirectional Lazy planner  
    *   sblprt: the probabilistic roadmap of trees (PRT) algorithm with SBL as the
        inter-root planner.  
    *   rrt*: the RRT* algorithm for optimal motion planning  
    *   prm*: the PRM* algorithm for optimal motion planning  
    *   lazyprm*: the Lazy-PRM* algorithm for optimal motion planning  
    *   lazyrrg*: the Lazy-RRG* algorithm for optimal motion planning  
    *   fmm: the fast marching method algorithm for resolution-complete optimal
        motion planning  
    *   fmm*: an anytime fast marching method algorithm for optimal motion planning  

    """
    return _motionplanning.setPlanType(type)

def setPlanSetting(*args):
    """
    setPlanSetting(char const * setting, double value)
    setPlanSetting(char const * setting, char const * value)



    Sets a numeric or string-valued setting for the planner.  

    Valid numeric values are:  

    *   "knn": k value for the k-nearest neighbor connection strategy (only for
        PRM)  
    *   "connectionThreshold": a milestone connection threshold  
    *   "perturbationRadius": (for RRT and SBL)  
    *   "bidirectional": 1 if bidirectional planning is requested (for RRT)  
    *   "grid": 1 if a point selection grid should be used (for SBL)  
    *   "gridResolution": resolution for the grid, if the grid should be used (for
        SBL with grid, FMM, FMM*)  
    *   "suboptimalityFactor": allowable suboptimality (for RRT*, lazy PRM*, lazy
        RRG*)  
    *   "randomizeFrequency": a grid randomization frequency (for SBL)  
    *   "shortcut": nonzero if you wish to perform shortcutting after a first plan
        is found.  
    *   "restart": nonzero if you wish to restart the planner to get better paths
        with the remaining time.  

    Valid string values are:  

    *   "pointLocation": a string designating a point location data structure.
        "kdtree" is supported, optionally followed by a weight vector (for PRM,
        RRT*, PRM*, LazyPRM*, LazyRRG*)  
    *   "restartTermCond": used if the "restart" setting is true. This is a JSON
        string defining the termination condition (default value:
        "{foundSolution:1;maxIters:1000}")  

    """
    return _motionplanning.setPlanSetting(*args)

def destroy():
    """
    destroy()



    destroys internal data structures  

    """
    return _motionplanning.destroy()
class CSpaceInterface(_object):
    """


    A raw interface for a configuration space. Note: the native Python CSpace
    interface class in cspace.py is easier to use.  

    You can either set a single feasibility test function using setFeasibility() or
    add several feasibility tests, all of which need to be satisfied, using
    addFeasibilityTest(). In the latter case, planners may be able to provide
    debugging statistics, solve Minimum Constraint Removal problems, run faster by
    eliminating constraint tests, etc.  

    Either setVisibility() or setVisibilityEpsilon() must be called to define a
    visibility checker between two (feasible) configurations. In the latter case,
    the path will be discretized at the resolution sent to setVisibilityEpsilon. If
    you have special single-constraint visibility tests, you can call that using
    addVisibilityTest (for example, for convex constraints you can set it to the
    lambda function that returns true regardless of its arguments).  

    Supported properties include "euclidean" (boolean), "metric" (string),
    "geodesic" (boolean), "minimum" (vector), and "maximum" (vector). These
    may be used by planners to make planning faster or more accurate. For a complete
    list see KrisLibrary/planning/CSpace.h.  

    C++ includes: motionplanning.h

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSpaceInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CSpaceInterface, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(CSpaceInterface self) -> CSpaceInterface
        __init__(CSpaceInterface self, CSpaceInterface arg2) -> CSpaceInterface



        """
        this = _motionplanning.new_CSpaceInterface(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _motionplanning.delete_CSpaceInterface
    __del__ = lambda self: None

    def destroy(self):
        """
        destroy(CSpaceInterface self)



        """
        return _motionplanning.CSpaceInterface_destroy(self)


    def setFeasibility(self, pyFeas):
        """
        setFeasibility(CSpaceInterface self, PyObject * pyFeas)



        """
        return _motionplanning.CSpaceInterface_setFeasibility(self, pyFeas)


    def addFeasibilityTest(self, name, pyFeas):
        """
        addFeasibilityTest(CSpaceInterface self, char const * name, PyObject * pyFeas)



        """
        return _motionplanning.CSpaceInterface_addFeasibilityTest(self, name, pyFeas)


    def setVisibility(self, pyVisible):
        """
        setVisibility(CSpaceInterface self, PyObject * pyVisible)



        """
        return _motionplanning.CSpaceInterface_setVisibility(self, pyVisible)


    def addVisibilityTest(self, name, pyVisible):
        """
        addVisibilityTest(CSpaceInterface self, char const * name, PyObject * pyVisible)



        """
        return _motionplanning.CSpaceInterface_addVisibilityTest(self, name, pyVisible)


    def setVisibilityEpsilon(self, eps):
        """
        setVisibilityEpsilon(CSpaceInterface self, double eps)



        """
        return _motionplanning.CSpaceInterface_setVisibilityEpsilon(self, eps)


    def setSampler(self, pySamp):
        """
        setSampler(CSpaceInterface self, PyObject * pySamp)



        """
        return _motionplanning.CSpaceInterface_setSampler(self, pySamp)


    def setNeighborhoodSampler(self, pySamp):
        """
        setNeighborhoodSampler(CSpaceInterface self, PyObject * pySamp)



        """
        return _motionplanning.CSpaceInterface_setNeighborhoodSampler(self, pySamp)


    def setDistance(self, pyDist):
        """
        setDistance(CSpaceInterface self, PyObject * pyDist)



        """
        return _motionplanning.CSpaceInterface_setDistance(self, pyDist)


    def setInterpolate(self, pyInterp):
        """
        setInterpolate(CSpaceInterface self, PyObject * pyInterp)



        """
        return _motionplanning.CSpaceInterface_setInterpolate(self, pyInterp)


    def setProperty(self, key, value):
        """
        setProperty(CSpaceInterface self, char const * key, char const * value)



        """
        return _motionplanning.CSpaceInterface_setProperty(self, key, value)


    def getProperty(self, key):
        """
        getProperty(CSpaceInterface self, char const * key) -> char const *



        """
        return _motionplanning.CSpaceInterface_getProperty(self, key)


    def isFeasible(self, q):
        """
        isFeasible(CSpaceInterface self, PyObject * q) -> bool



        Queries whether a given configuration is feasible.  

        """
        return _motionplanning.CSpaceInterface_isFeasible(self, q)


    def isVisible(self, a, b):
        """
        isVisible(CSpaceInterface self, PyObject * a, PyObject * b) -> bool



        Queries whether two configurations are visible.  

        """
        return _motionplanning.CSpaceInterface_isVisible(self, a, b)


    def testFeasibility(self, name, q):
        """
        testFeasibility(CSpaceInterface self, char const * name, PyObject * q) -> bool



        Queries whether a given configuration is feasible with respect to a given
        constraint.  

        """
        return _motionplanning.CSpaceInterface_testFeasibility(self, name, q)


    def testVisibility(self, name, a, b):
        """
        testVisibility(CSpaceInterface self, char const * name, PyObject * a, PyObject * b) -> bool



        Queries whether two configurations are visible with respect to a given
        constraint.  

        """
        return _motionplanning.CSpaceInterface_testVisibility(self, name, a, b)


    def feasibilityFailures(self, q):
        """
        feasibilityFailures(CSpaceInterface self, PyObject * q) -> PyObject *



        Returns a list of all failed feasibility constraints.  

        """
        return _motionplanning.CSpaceInterface_feasibilityFailures(self, q)


    def visibilityFailures(self, a, b):
        """
        visibilityFailures(CSpaceInterface self, PyObject * a, PyObject * b) -> PyObject *



        Returns a list of all failed visibility constraints.  

        """
        return _motionplanning.CSpaceInterface_visibilityFailures(self, a, b)


    def sample(self):
        """
        sample(CSpaceInterface self) -> PyObject *



        Samples a configuration.  

        """
        return _motionplanning.CSpaceInterface_sample(self)


    def distance(self, a, b):
        """
        distance(CSpaceInterface self, PyObject * a, PyObject * b) -> double



        Returns the distance between two configurations.  

        """
        return _motionplanning.CSpaceInterface_distance(self, a, b)


    def interpolate(self, a, b, u):
        """
        interpolate(CSpaceInterface self, PyObject * a, PyObject * b, double u) -> PyObject *



        Interpolates between two configurations.  

        """
        return _motionplanning.CSpaceInterface_interpolate(self, a, b, u)


    def adaptiveQueriesEnabled(self):
        """
        adaptiveQueriesEnabled(CSpaceInterface self) -> bool



        optional: adaptive queries can be used to automatically minimize the total cost
        of testing feasibility / visibility using empirical estimates. Off by default.  

        """
        return _motionplanning.CSpaceInterface_adaptiveQueriesEnabled(self)


    def enableAdaptiveQueries(self, enabled=True):
        """
        enableAdaptiveQueries(CSpaceInterface self, bool enabled=True)
        enableAdaptiveQueries(CSpaceInterface self)



        Call this to enable adaptive queries. (It has a small overhead.)  

        """
        return _motionplanning.CSpaceInterface_enableAdaptiveQueries(self, enabled)


    def optimizeQueryOrder(self):
        """
        optimizeQueryOrder(CSpaceInterface self)



        Call this to optimize the feasibility / visibility testing order.  

        """
        return _motionplanning.CSpaceInterface_optimizeQueryOrder(self)


    def setFeasibilityDependency(self, name, precedingTest):
        """
        setFeasibilityDependency(CSpaceInterface self, char const * name, char const * precedingTest)



        Marks that a certain feasibility test must be performed before another.  

        """
        return _motionplanning.CSpaceInterface_setFeasibilityDependency(self, name, precedingTest)


    def setFeasibilityPrior(self, name, costPrior=0.0, feasibilityProbability=0.0, evidenceStrength=1.0):
        """
        setFeasibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0, double feasibilityProbability=0.0, double evidenceStrength=1.0)
        setFeasibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0, double feasibilityProbability=0.0)
        setFeasibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0)
        setFeasibilityPrior(CSpaceInterface self, char const * name)



        Resets the data for a certain feasibility test. Default values give a data-
        gathering behavior.  

        """
        return _motionplanning.CSpaceInterface_setFeasibilityPrior(self, name, costPrior, feasibilityProbability, evidenceStrength)


    def setVisibilityDependency(self, name, precedingTest):
        """
        setVisibilityDependency(CSpaceInterface self, char const * name, char const * precedingTest)



        Marks that a certain feasibility test must be performed before another.  

        """
        return _motionplanning.CSpaceInterface_setVisibilityDependency(self, name, precedingTest)


    def setVisibilityPrior(self, name, costPrior=0.0, visibilityProbability=0.0, evidenceStrength=1.0):
        """
        setVisibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0, double visibilityProbability=0.0, double evidenceStrength=1.0)
        setVisibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0, double visibilityProbability=0.0)
        setVisibilityPrior(CSpaceInterface self, char const * name, double costPrior=0.0)
        setVisibilityPrior(CSpaceInterface self, char const * name)



        Resets the data for a certain visibility test. Default values give a data-
        gathering behavior.  

        """
        return _motionplanning.CSpaceInterface_setVisibilityPrior(self, name, costPrior, visibilityProbability, evidenceStrength)


    def feasibilityCost(self, name):
        """
        feasibilityCost(CSpaceInterface self, char const * name) -> double



        Retrieves the empirical average cost of a given feasibility test.  

        """
        return _motionplanning.CSpaceInterface_feasibilityCost(self, name)


    def feasibilityProbability(self, name):
        """
        feasibilityProbability(CSpaceInterface self, char const * name) -> double



        Retrieves the empirical average success rate of a given feasibility test.  

        """
        return _motionplanning.CSpaceInterface_feasibilityProbability(self, name)


    def visibilityCost(self, name):
        """
        visibilityCost(CSpaceInterface self, char const * name) -> double



        Retrieves the empirical average cost of a given visibility test.  

        """
        return _motionplanning.CSpaceInterface_visibilityCost(self, name)


    def visibilityProbability(self, name):
        """
        visibilityProbability(CSpaceInterface self, char const * name) -> double



        Retrieves the empirical average success rate of a given visibility test.  

        """
        return _motionplanning.CSpaceInterface_visibilityProbability(self, name)


    def feasibilityQueryOrder(self):
        """
        feasibilityQueryOrder(CSpaceInterface self) -> PyObject *



        Retrieves the current order of feasibility tests.  

        """
        return _motionplanning.CSpaceInterface_feasibilityQueryOrder(self)


    def visibilityQueryOrder(self):
        """
        visibilityQueryOrder(CSpaceInterface self) -> PyObject *



        Retrieves the current order of visibility tests.  

        """
        return _motionplanning.CSpaceInterface_visibilityQueryOrder(self)


    def getStats(self):
        """
        getStats(CSpaceInterface self) -> PyObject *



        Returns constraint testing statistics. If adaptive queries are enabled, this
        returns the stats on each constraint.  

        """
        return _motionplanning.CSpaceInterface_getStats(self)

    __swig_setmethods__["index"] = _motionplanning.CSpaceInterface_index_set
    __swig_getmethods__["index"] = _motionplanning.CSpaceInterface_index_get
    if _newclass:
        index = _swig_property(_motionplanning.CSpaceInterface_index_get, _motionplanning.CSpaceInterface_index_set)
CSpaceInterface_swigregister = _motionplanning.CSpaceInterface_swigregister
CSpaceInterface_swigregister(CSpaceInterface)

class PlannerInterface(_object):
    """


    An interface for a kinematic motion planner. The :class:`MotionPlan` interface
    in cspace.py is somewhat easier to use.  

    On construction, uses the planner type specified by setPlanType and the settings
    currently specified by calls to setPlanSetting.  

    Point-to-point planning is enabled by sending two configurations to the
    setEndpoints method. This is mandatory for RRT and SBL-style planners. The start
    and end milestones are given by indices 0 and 1, respectively  

    Point-to-set planning is enabled by sending a *goal test* as the second argument
    to the setEndpoints method. It is possible also to send a special goal sampler
    by providing a *pair of functions* as the second argument consisting of the two
    functions (goaltest,goalsample). The first in this pair tests whether a
    configuration is a goal, and the second returns a sampled configuration in a
    superset of the goal. Ideally the goal sampler generates as many goals as
    possible.  

    To plan, call planMore(iters) until getPath(0,1) returns non-NULL. The return
    value is a list of configurations.  

    Some planners can be used multi-query mode (such as PRM). In multi-query mode,
    you may call addMilestone(q) to add a new milestone. addMilestone() returns the
    index of that milestone, which can be used in later calls to getPath().  

    In point-to-set mode, getSolutionPath will return the optimal path to any goal
    milestone.  

    All planners work with the standard path-length objective function. Some
    planners can work with other cost functions, and you can use setCostFunction to
    set the edge / terminal costs. Usually, the results will only be optimal on the
    computed graph, and the graph is not specifically computed to optimize that
    cost.  

    To get a roadmap (V,E), call getRoadmap(). V is a list of configurations (each
    configuration is a Python list) and E is a list of edges (each edge is a pair
    (i,j) indexing into V).  

    To dump the roadmap to disk, call dump(fn). This saves to a Trivial Graph Format
    (TGF) format.  

    C++ includes: motionplanning.h

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PlannerInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PlannerInterface, name)
    __repr__ = _swig_repr

    def __init__(self, cspace):
        """
        __init__(PlannerInterface self, CSpaceInterface cspace) -> PlannerInterface



        """
        this = _motionplanning.new_PlannerInterface(cspace)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _motionplanning.delete_PlannerInterface
    __del__ = lambda self: None

    def destroy(self):
        """
        destroy(PlannerInterface self)



        """
        return _motionplanning.PlannerInterface_destroy(self)


    def setEndpoints(self, start, goal):
        """
        setEndpoints(PlannerInterface self, PyObject * start, PyObject * goal) -> bool



        """
        return _motionplanning.PlannerInterface_setEndpoints(self, start, goal)


    def setEndpointSet(self, start, goal, goalSample=None):
        """
        setEndpointSet(PlannerInterface self, PyObject * start, PyObject * goal, PyObject * goalSample=None) -> bool
        setEndpointSet(PlannerInterface self, PyObject * start, PyObject * goal) -> bool



        """
        return _motionplanning.PlannerInterface_setEndpointSet(self, start, goal, goalSample)


    def setCostFunction(self, edgeCost=None, terminalCost=None):
        """
        setCostFunction(PlannerInterface self, PyObject * edgeCost=None, PyObject * terminalCost=None)
        setCostFunction(PlannerInterface self, PyObject * edgeCost=None)
        setCostFunction(PlannerInterface self)



        """
        return _motionplanning.PlannerInterface_setCostFunction(self, edgeCost, terminalCost)


    def addMilestone(self, milestone):
        """
        addMilestone(PlannerInterface self, PyObject * milestone) -> int



        """
        return _motionplanning.PlannerInterface_addMilestone(self, milestone)


    def getClosestMilestone(self, config):
        """
        getClosestMilestone(PlannerInterface self, PyObject * config) -> int



        """
        return _motionplanning.PlannerInterface_getClosestMilestone(self, config)


    def getMilestone(self, arg2):
        """
        getMilestone(PlannerInterface self, int arg2) -> PyObject *



        """
        return _motionplanning.PlannerInterface_getMilestone(self, arg2)


    def planMore(self, iterations):
        """
        planMore(PlannerInterface self, int iterations)



        """
        return _motionplanning.PlannerInterface_planMore(self, iterations)


    def getSolutionPath(self):
        """
        getSolutionPath(PlannerInterface self) -> PyObject *



        """
        return _motionplanning.PlannerInterface_getSolutionPath(self)


    def getPath(self, *args):
        """
        getPath(PlannerInterface self, int milestone1, int milestone2) -> PyObject
        getPath(PlannerInterface self, int milestone1, std::vector< int,std::allocator< int > > const & goalMilestones) -> PyObject *



        """
        return _motionplanning.PlannerInterface_getPath(self, *args)


    def getData(self, setting):
        """
        getData(PlannerInterface self, char const * setting) -> double



        """
        return _motionplanning.PlannerInterface_getData(self, setting)


    def getStats(self):
        """
        getStats(PlannerInterface self) -> PyObject *



        """
        return _motionplanning.PlannerInterface_getStats(self)


    def getRoadmap(self):
        """
        getRoadmap(PlannerInterface self) -> PyObject *



        """
        return _motionplanning.PlannerInterface_getRoadmap(self)


    def dump(self, fn):
        """
        dump(PlannerInterface self, char const * fn)



        """
        return _motionplanning.PlannerInterface_dump(self, fn)

    __swig_setmethods__["index"] = _motionplanning.PlannerInterface_index_set
    __swig_getmethods__["index"] = _motionplanning.PlannerInterface_index_get
    if _newclass:
        index = _swig_property(_motionplanning.PlannerInterface_index_get, _motionplanning.PlannerInterface_index_set)
    __swig_setmethods__["spaceIndex"] = _motionplanning.PlannerInterface_spaceIndex_set
    __swig_getmethods__["spaceIndex"] = _motionplanning.PlannerInterface_spaceIndex_get
    if _newclass:
        spaceIndex = _swig_property(_motionplanning.PlannerInterface_spaceIndex_get, _motionplanning.PlannerInterface_spaceIndex_set)
PlannerInterface_swigregister = _motionplanning.PlannerInterface_swigregister
PlannerInterface_swigregister(PlannerInterface)

# This file is compatible with both classic and new-style classes.


