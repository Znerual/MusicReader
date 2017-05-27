def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)
class _CONST:
    @constant
    def WIDTH():
        return 128
    @constant
    def HEIGHT():
        return 128
    @constant
    def MAX_STEP_SIZE():
        return 20
    @constant
    def GOAL():
        return (64,64)
    @constant
    def MAX_ITERATION_LENGTH():
        return 500
