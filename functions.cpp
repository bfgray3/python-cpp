#include <thread>

#ifdef __cplusplus
extern "C" {
#endif

int f(int n) {
  int i = 0;
  for (int j = 0; j < n; ++j) {
    ++i;
  }
  return i;
}

int f_async(int n) {
  // TODO
  return n;
}

int f_threads(int n) {
  // TODO: try jthread
  std::thread t1{f, n}, t2{f, n};
  t1.join();
  t2.join();
  return 0;
}

#ifdef __cplusplus
}
#endif
