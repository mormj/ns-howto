#pragma once

#include <gnuradio/howto/copy.hh>

namespace gr {
namespace howto {

class copy_cpu : public copy
{
public:
    copy_cpu(block_args args) : sync_block("copy"), copy(args), d_itemsize(args.itemsize) {}
    virtual work_return_code_t work(std::vector<block_work_input>& work_input,
                                    std::vector<block_work_output>& work_output) override;

protected:
    size_t d_itemsize;
};

} // namespace howto
} // namespace gr