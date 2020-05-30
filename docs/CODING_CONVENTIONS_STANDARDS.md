# Bkliz Coding Conventions and Standards


## C++ Code Style

Google style from https://google.github.io/styleguide/cppguide.html with a few minor alterations:

* Max line length 120
  *	Aim for 80, but up to 120 is fine.
* Exceptions
  *	Allowed to throw fatal errors that are expected to result in a top level handler catching them, logging them and terminating the program.
* Non-const references
  *	Allowed
  * Use a non-const reference for arguments that are modifiable but cannot be nullptr so the API clearly advertises the intent
  *	Const correctness and usage of smart pointers (shared_ptr and unique_ptr) is expected. A non-const reference equates to “this is a non-null object that you can change but are not being given ownership of”.
* 'using namespace' permitted with limited scope
  * Not allowing 'using namespace' at all is overly restrictive. Follow the C++ Core Guidelines:
    * [SF.6: Use using namespace directives for transition, for foundation libraries (such as std), or within a local scope (only)](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#Rs-using)
    * [SF.7: Don't write using namespace at global scope in a header file](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#Rs-using-directive)

Other
* Qualify usages of 'auto' with 'const', '*', '&' and '&&' where applicable to more clearly express the intent
* When adding a new class, disable copy/assignment/move until you have a proven need for these capabilities. If a need arises, enable copy/assignment/move selectively, and when doing so validate that the implementation of the class supports what is being enabled.
  * Use ORT_DISALLOW_COPY_ASSIGNMENT_AND_MOVE initially
  * See the other ORT_DISALLOW_* macros in https://github.com/microsoft/onnxruntime/blob/master/include/onnxruntime/core/common/common.h
* Don't use else after return. see: [https://llvm.org/docs/CodingStandards.html#don-t-use-else-after-a-return](https://llvm.org/docs/CodingStandards.html#don-t-use-else-after-a-return)
* Don't overuse std::shared\_ptr. Use std::shared\_ptr only if it's not clear when and where the object will be deallocated. See also: [https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-shared_ptr](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-shared_ptr)
* Avoid using the 'long' type, which could be either 32 bits or 64 bits.
* If there is a legitimate need to allocate objects on the heap, prefer using onnxruntime::make_unique(). References for the reasoning:
  * https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#Rh-make_unique
  * https://herbsutter.com/2013/05/29/gotw-89-solution-smart-pointers/
  * https://abseil.io/tips/126
* Use [SafeInt](https://github.com/dcleblanc/SafeInt) when calculating the size of memory to allocate to protect against overflow errors
  * `#include "core/common/safeint.h"`
  * search for `SafeInt<size_t>` in the code for examples

## Python Code Style

Please adhere to the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/).
A maximum line length of 120 characters is allowed for consistency with the C++ code.

Code can be validated with [flake8](https://pypi.org/project/flake8/) using the configuration file in the root directory called [.flake8](https://github.com/microsoft/onnxruntime/tree/master/.flake8).

The [autopep8](https://pypi.org/project/autopep8/) tool can be used to automatically fix a range of PEP8 issues, as can [yapf](https://github.com/google/yapf). There's a yapf configuration file [here](https://github.com/microsoft/onnxruntime/tree/master/onnxruntime/.style.yapf).

Editors such as PyCharm [(see here)](https://www.jetbrains.com/help/pycharm/code-inspection.html) and Visual Studio Code [(see here)](https://code.visualstudio.com/docs/python/linting#_flake8) can be configured to check for PEP8 issues.
