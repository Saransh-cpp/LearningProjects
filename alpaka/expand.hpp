// #pragma once
// #include <alpaka/alpaka.hpp>

// namespace alpaka_kernels {

// op = "\n//------ Expand_KERNEL_ALPAKA\n";
// struct ExpandKernel {
//     template<typename TAcc, typename T>
//     ALPAKA_FN_ACC void operator()(TAcc const & acc, T const * input, T * output, const size_t * input_shape, const size_t * output_shape, const size_t * input_strides, const size_t * output_strides, const alpaka::trait::DimType<int> ndim){
//         size_t input_idx = 0;
//         size_t output_idx = 0;
//         size_t coord_out;
//         size_t coord_in;
//         auto elements = alpaka::uniformElementsND(acc, alpaka::Vec<alpaka::DimInt<1>, std::size_t>(output_shape));
//         for (auto const& elem : elements) {
//             input_idx = 0;
//             output_idx = 0;
//             for (int i = 0; i < ndim; ++i) {
//                 coord_out = elem[i];
//                 coord_in = (input_shape[i] == 1) ? 0 : coord_out;
//                 input_idx += coord_in * input_strides[i];
//                 output_idx += coord_out * output_strides[i];
//             }
//             output[output_idx] = input[input_idx];
//         }
//     }
// };
// } // namespace alpaka_kernels
