# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, render_metric_string_list_to_input_args_kwargs


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.aten.clone.default(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "metrics-autogen-op/ALL", "aten.clone.default")


@pytest.mark.parametrize(
    "input_strings",
    [
        ["Tensor<[1, 256, 1024]> self = ?"],
        ["Tensor<[1, 16, 256, 256]> self = ?"],
        ["Tensor<[1, 256, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 32, 32]> self = ?"],
        ["Tensor<[1, 32, 16, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 1536]> self = ?"],
        ["Tensor<[1, 12, 50, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[12, 50, 50]> self = ?"],
        ["Tensor<[1, 50, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[2, 8, 7, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 7, 7]> self = ?"],
        ["Tensor<[2, 7, 8, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[2, 7, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[920, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[920, 1, 256]> self = ?"],
        ["Tensor<[920, 1, 2048]> self = ?"],
        ["Tensor<[100, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[100, 1, 256]> self = ?"],
        ["Tensor<[100, 1, 2048]> self = ?"],
        ["Tensor<[1, 25, 768]> self = ?"],
        ["Tensor<[1, 12, 25, 25]> self = ?"],
        ["Tensor<[1, 25, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 25]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 15, 512]> self = ?"],
        ["Tensor<[1, 6, 15, 15]> self = ?"],
        ["Tensor<[1, 15, 6, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 15, 1024]> self = ?"],
        ["Tensor<[1, 1, 512]> self = ?"],
        ["Tensor<[1, 6, 1, 1]> self = ?"],
        ["Tensor<[1, 6, 1, 15]> self = ?"],
        ["Tensor<[1, 1, 1024]> self = ?"],
        ["Tensor<[1, 6, 1, 2]> self = ?"],
        ["Tensor<[1, 6, 1, s0 + 1]> self = ?"],
        ["Tensor<[1, 6, 1, 17]> self = ?"],
        ["Tensor<[1, 1, 19200, 300]> self = ?"],
        ["Tensor<[1, 19200, 64]> self = ?"],
        ["Tensor<[1, 19200, 256]> self = ?"],
        ["Tensor<[1, 64, 120, 160]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 4800, 300]> self = ?"],
        ["Tensor<[1, 4800, 2, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4800, 128]> self = ?"],
        ["Tensor<[1, 4800, 512]> self = ?"],
        ["Tensor<[1, 128, 60, 80]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 5, 1200, 300]> self = ?"],
        ["Tensor<[1, 1200, 5, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1200, 320]> self = ?"],
        ["Tensor<[1, 1200, 1280]> self = ?"],
        ["Tensor<[1, 320, 30, 40]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 300, 300]> self = ?"],
        ["Tensor<[1, 300, 8, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 300, 512]> self = ?"],
        ["Tensor<[1, 300, 2048]> self = ?"],
        ["Tensor<[1, 512, 15, 20]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 7, 768]> self = ?"],
        ["Tensor<[1, 12, 7, 7]> self = ?"],
        ["Tensor<[1, 7, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1, 45]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 45, 768]> self = ?"],
        ["Tensor<[1, 12, 45, 45]> self = ?"],
        ["Tensor<[1, 45, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1, 768]> self = ?"],
        ["Tensor<[1, 12, 1, 46]> self = ?"],
        ["Tensor<[1, s10 + 1]> self = ?"],
        ["Tensor<[1, 12, 1, s10 + 1]> self = ?"],
        ["Tensor<[1, 1024]> self = ?"],
        ["Tensor<[1, 16, 16, 16, 16, 3]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1024, 512]> self = ?"],
        ["Tensor<[1, 256, 512]> self = ?"],
        ["Tensor<[1, 256, 256]> self = ?"],
        ["Tensor<[1, 3, 16, 16, 16, 16]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 64, 12, 12]> self = ?"],
        ["Tensor<[1, 128]> self = ?"],
        ["Tensor<[1, 20, 20, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 10, 10, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 5, 5, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 3, 3, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 20, 20, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 10, 10, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 5, 5, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 3, 3, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[20, 20]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[10, 10]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[5, 5]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[3, 3]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[2, 2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1280]> self = ?"],
        ["Tensor<[1, 16, 59, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 59, 59]> self = ?"],
        ["Tensor<[1, 59, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 59, 1024]> self = ?"],
        ["Tensor<[59, 1024]> self = ?"],
        ["Tensor<[16, 1, 60]> self = ?"],
        ["Tensor<[16, 1, s10 + 1]> self = ?"],
        ["Tensor<[1, 8, 256, 2048]> self = ?"],
        ["Tensor<[1, 256, 8, 160]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 256, 256]> self = ?"],
        ["Tensor<[1, 8, 2048, 256]> self = ?"],
        ["Tensor<[1, 2048, 8, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 10, 768]> self = ?"],
        ["Tensor<[1, 12, 10, 10]> self = ?"],
        ["Tensor<[1, 10, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1, 16384, 256]> self = ?"],
        ["Tensor<[1, 16384, 32]> self = ?"],
        ["Tensor<[1, 16384, 128]> self = ?"],
        ["Tensor<[1, 32, 128, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 4096, 256]> self = ?"],
        ["Tensor<[1, 4096, 2, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4096, 64]> self = ?"],
        ["Tensor<[1, 4096, 256]> self = ?"],
        ["Tensor<[1, 64, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 5, 1024, 256]> self = ?"],
        ["Tensor<[1, 1024, 5, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1024, 160]> self = ?"],
        ["Tensor<[1, 1024, 640]> self = ?"],
        ["Tensor<[1, 160, 32, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 256, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 256, 16, 16]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 256, 128, 128]> self = ?", "Optional[int] memory_format = torch.channels_last"],
        ["Tensor<[1, 256, 128, 128]> self = ?"],
        ["Tensor<[1, 256, 5, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 256, 2, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 768]> self = ?"],
        ["Tensor<[1, 320, 64, 64]> self = ?"],
        ["Tensor<[1, 4096, 320]> self = ?"],
        ["Tensor<[1, 4096, 1280]> self = ?"],
        ["Tensor<[1, 320, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 640, s0, s1]> self = ?"],
        ["Tensor<[1, s0*s1, 640]> self = ?"],
        ["Tensor<[1, s0*s1, 2560]> self = ?"],
        ["Tensor<[1, 640, s0, s1]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1280, s1, s2]> self = ?"],
        ["Tensor<[1, s1*s2, 1280]> self = ?"],
        ["Tensor<[1, s1*s2, 5120]> self = ?"],
        ["Tensor<[1, 1280, s1, s2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1280, s0, s1]> self = ?"],
        ["Tensor<[1, s0*s1, 1280]> self = ?"],
        ["Tensor<[1, s0*s1, 5120]> self = ?"],
        ["Tensor<[1, 1280, s0, s1]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1280, 8, 8]> self = ?"],
        ["Tensor<[1, 640, s1, s2]> self = ?"],
        ["Tensor<[1, s1*s2, 640]> self = ?"],
        ["Tensor<[1, s1*s2, 2560]> self = ?"],
        ["Tensor<[1, 640, s1, s2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 320, s1, s2]> self = ?"],
        ["Tensor<[1, s1*s2, 320]> self = ?"],
        ["Tensor<[1, 320, s1, s2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1500, 768]> self = ?"],
        ["Tensor<[1, 12, 1500, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1500, 3072]> self = ?"],
        ["Tensor<[1, 1, 3072]> self = ?"],
        ["Tensor<[1, 4, 768]> self = ?"],
        ["Tensor<[1, 12, 4, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 3072]> self = ?"],
        ["Tensor<[1, 19, 1024]> self = ?"],
        ["Tensor<[1, 16, 19, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 19, 19]> self = ?"],
        ["Tensor<[1, 19, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 19, 4096]> self = ?"],
        ["Tensor<[1, 192, 32, 42]> self = ?", "Optional[int] memory_format = torch.channels_last"],
        ["Tensor<[1, 1445, 192]> self = ?"],
        ["Tensor<[1, 3, 1445, 1445]> self = ?"],
        ["Tensor<[1, 1445, 3, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 9, 128]> self = ?"],
        ["Tensor<[1, 12, 9, 9]> self = ?"],
        ["Tensor<[1, 9, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 9, 768]> self = ?"],
        ["Tensor<[1, 12, 128]> self = ?"],
        ["Tensor<[1, 12, 12, 12]> self = ?"],
        ["Tensor<[1, 12, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 12, 768]> self = ?"],
        ["Tensor<[1, 16, 9, 9]> self = ?"],
        ["Tensor<[1, 9, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 9, 1024]> self = ?"],
        ["Tensor<[1, 9, 16, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 9, 2048]> self = ?"],
        ["Tensor<[1, 64, 9, 9]> self = ?"],
        ["Tensor<[1, 9, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 9, 4096]> self = ?"],
        ["Tensor<[1, 5, 1024]> self = ?"],
        ["Tensor<[1, 5, 4, 4, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 5, 1, 16, 2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 5, 5]> self = ?"],
        ["Tensor<[1, 5, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1, 4, 4, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1, 1, 16, 2]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 1, 6]> self = ?"],
        ["Tensor<[1, 16, 1, s10 + 1]> self = ?"],
        ["Tensor<[1, 16, 768]> self = ?"],
        ["Tensor<[1, 12, 16, 16]> self = ?"],
        ["Tensor<[1, 16, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 512, 1, 1]> self = ?"],
        ["Tensor<[1, 197, 768]> self = ?"],
        ["Tensor<[1, 12, 197, 197]> self = ?"],
        ["Tensor<[1, 197, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 160, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 112, 14, 14]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 80, 14, 14]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 40, 28, 28]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 56, 56]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 112, 112]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2048]> self = ?"],
        ["Tensor<[1, 1536]> self = ?"],
        ["Tensor<[12, 197, 197]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 197, 1024]> self = ?"],
        ["Tensor<[16, 197, 197]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 197, 197]> self = ?"],
        ["Tensor<[1, 197, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 768, 384]> self = ?"],
        ["Tensor<[1, 768, 196]> self = ?"],
        ["Tensor<[1, 196, 3072]> self = ?"],
        ["Tensor<[1, 196, 768]> self = ?"],
        ["Tensor<[1, 768]> self = ?"],
        ["Tensor<[1, 100, 136, 9, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 50, 68, 9, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 25, 34, 9, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 13, 17, 9, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 7, 9, 9, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 100, 136, 9, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 50, 68, 9, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 25, 34, 9, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 13, 17, 9, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 7, 9, 9, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[100, 136]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[50, 68]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[25, 34]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[13, 17]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[7, 9]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 768]> self = ?"],
        ["Tensor<[1, 12, 24, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[12, 24, 24]> self = ?"],
        ["Tensor<[1, 24, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 3072]> self = ?"],
        ["Tensor<[1, 38, 38, 4, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 19, 19, 6, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 3, 3, 4, 4]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 38, 38, 4, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 19, 19, 6, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 3, 3, 4, 91]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[38, 38]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[19, 19]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 7, 7, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 49, 49]> self = ?"],
        ["Tensor<[64, 49, 4, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 49, 128]> self = ?"],
        ["Tensor<[1, 8, 7, 8, 7, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 56, 56, 512]> self = ?"],
        ["Tensor<[1, 56, 56, 128]> self = ?"],
        ["Tensor<[8, 8, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[8, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 7, 7, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 49, 49]> self = ?"],
        ["Tensor<[16, 49, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 49, 256]> self = ?"],
        ["Tensor<[1, 4, 7, 4, 7, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 28, 28, 1024]> self = ?"],
        ["Tensor<[1, 28, 28, 256]> self = ?"],
        ["Tensor<[4, 4, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 7, 7, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 49, 49]> self = ?"],
        ["Tensor<[4, 49, 16, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 49, 512]> self = ?"],
        ["Tensor<[1, 2, 7, 2, 7, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 14, 14, 2048]> self = ?"],
        ["Tensor<[1, 14, 14, 512]> self = ?"],
        ["Tensor<[2, 2, 7, 7]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[32, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 49, 49]> self = ?"],
        ["Tensor<[1, 49, 32, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 49, 1024]> self = ?"],
        ["Tensor<[1, 7, 7, 4096]> self = ?"],
        ["Tensor<[1, 7, 7, 1024]> self = ?"],
        ["Tensor<[3, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 7, 7, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 49, 49]> self = ?"],
        ["Tensor<[64, 49, 3, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 49, 96]> self = ?"],
        ["Tensor<[1, 8, 7, 8, 7, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 56, 56, 384]> self = ?"],
        ["Tensor<[1, 56, 56, 96]> self = ?"],
        ["Tensor<[6, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 7, 7, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 49, 49]> self = ?"],
        ["Tensor<[16, 49, 6, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 49, 192]> self = ?"],
        ["Tensor<[1, 4, 7, 4, 7, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 28, 28, 768]> self = ?"],
        ["Tensor<[1, 28, 28, 192]> self = ?"],
        ["Tensor<[12, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 7, 7, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 49, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 32, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 49, 49]> self = ?"],
        ["Tensor<[4, 49, 12, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 49, 384]> self = ?"],
        ["Tensor<[1, 2, 7, 2, 7, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 14, 14, 1536]> self = ?"],
        ["Tensor<[1, 14, 14, 384]> self = ?"],
        ["Tensor<[24, 49, 49]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 49, 49]> self = ?"],
        ["Tensor<[1, 49, 24, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 49, 768]> self = ?"],
        ["Tensor<[1, 7, 7, 3072]> self = ?"],
        ["Tensor<[1, 7, 7, 768]> self = ?"],
        ["Tensor<[4, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 4, 64, 64]> self = ?"],
        ["Tensor<[64, 64, 4, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 64, 128]> self = ?"],
        ["Tensor<[1, 64, 64, 512]> self = ?"],
        ["Tensor<[1, 64, 64, 128]> self = ?"],
        ["Tensor<[8, 8, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[8, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 8, 64, 64]> self = ?"],
        ["Tensor<[16, 64, 8, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 64, 256]> self = ?"],
        ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 32, 1024]> self = ?"],
        ["Tensor<[1, 32, 32, 256]> self = ?"],
        ["Tensor<[4, 4, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 16, 64, 64]> self = ?"],
        ["Tensor<[4, 64, 16, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 64, 512]> self = ?"],
        ["Tensor<[1, 2, 8, 2, 8, 512]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 16, 2048]> self = ?"],
        ["Tensor<[1, 16, 16, 512]> self = ?"],
        ["Tensor<[2, 2, 8, 8]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[32, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 64, 64]> self = ?"],
        ["Tensor<[1, 64, 32, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 64, 1024]> self = ?"],
        ["Tensor<[1, 8, 8, 4096]> self = ?"],
        ["Tensor<[1, 8, 8, 1024]> self = ?"],
        ["Tensor<[3, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 3, 64, 64]> self = ?"],
        ["Tensor<[64, 64, 3, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[64, 64, 96]> self = ?"],
        ["Tensor<[1, 64, 64, 384]> self = ?"],
        ["Tensor<[1, 64, 64, 96]> self = ?"],
        ["Tensor<[6, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 6, 64, 64]> self = ?"],
        ["Tensor<[16, 64, 6, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[16, 64, 192]> self = ?"],
        ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 32, 32, 768]> self = ?"],
        ["Tensor<[1, 32, 32, 192]> self = ?"],
        ["Tensor<[12, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 64, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 32, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 12, 64, 64]> self = ?"],
        ["Tensor<[4, 64, 12, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[4, 64, 384]> self = ?"],
        ["Tensor<[1, 2, 8, 2, 8, 384]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 16, 16, 1536]> self = ?"],
        ["Tensor<[1, 16, 16, 384]> self = ?"],
        ["Tensor<[24, 64, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 24, 64, 64]> self = ?"],
        ["Tensor<[1, 64, 24, 32]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 64, 768]> self = ?"],
        ["Tensor<[1, 8, 8, 3072]> self = ?"],
        ["Tensor<[1, 8, 8, 768]> self = ?"],
        ["Tensor<[1, 10, 3072]> self = ?"],
        ["Tensor<[1, 12, 1, 1]> self = ?"],
        ["Tensor<[1, 12, 1, 10]> self = ?"],
        ["Tensor<[1, 12, 1, 2]> self = ?"],
        ["Tensor<[1, 12, 1, s0 + 1]> self = ?"],
        ["Tensor<[1, 10, 1024]> self = ?"],
        ["Tensor<[1, 16, 10, 10]> self = ?"],
        ["Tensor<[1, 10, 16, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 10, 4096]> self = ?"],
        ["Tensor<[1, 16, 1, 1]> self = ?"],
        ["Tensor<[1, 16, 1, 10]> self = ?"],
        ["Tensor<[1, 1, 4096]> self = ?"],
        ["Tensor<[1, 16, 1, 2]> self = ?"],
        ["Tensor<[1, 16, 1, s0 + 1]> self = ?"],
        ["Tensor<[1, 10, 512]> self = ?"],
        ["Tensor<[1, 8, 10, 10]> self = ?"],
        ["Tensor<[1, 10, 8, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 10, 2048]> self = ?"],
        ["Tensor<[1, 8, 1, 1]> self = ?"],
        ["Tensor<[1, 8, 1, 10]> self = ?"],
        ["Tensor<[1, 1, 2048]> self = ?"],
        ["Tensor<[1, 8, 1, 2]> self = ?"],
        ["Tensor<[1, 8, 1, s0 + 1]> self = ?"],
        ["Tensor<[1, 14, 128]> self = ?"],
        ["Tensor<[1, 12, 14, 14]> self = ?"],
        ["Tensor<[1, 14, 12, 64]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 14, 768]> self = ?"],
        ["Tensor<[1, 14]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 4096]> self = ?"],
        ["Tensor<[3, 197, 1, 768]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 197, 3072]> self = ?"],
        ["Tensor<[1, 50, 768]> self = ?"],
        ["Tensor<[3, 50, 1, 768]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 50, 3072]> self = ?"],
        ["Tensor<[1, 1370, 1280]> self = ?"],
        ["Tensor<[3, 1370, 1, 1280]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 1370, 5120]> self = ?"],
        ["Tensor<[3, 197, 1, 1024]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 197, 4096]> self = ?"],
        ["Tensor<[1, 50, 1024]> self = ?"],
        ["Tensor<[3, 50, 1, 1024]> self = ?", "Optional[int] memory_format = torch.contiguous_format"],
        ["Tensor<[1, 50, 4096]> self = ?"],
    ],
)
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {
        "opname": "aten.clone.default",
        "input_strings": input_strings,
        "native_run": "N/A",
        "run": "N/A",
        "accuracy": "N/A",
        "convert_to_ttnn": "N/A",
        "ttnn_fallbacks_to_host_count": "N/A",
    }
    m = AtenModule()
    input_args, input_kwargs, status = render_metric_string_list_to_input_args_kwargs(
        "aten.clone.default", input_strings
    )
    if status == False:
        pytest.skip("Invalid input strings")
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {e}")
        metric["native_run"] = False

    if metric["native_run"] == True:
        result_after = None
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            ttnn.graph.begin_graph_capture()
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {e}")
            metric["run"] = False
        finally:
            trace = ttnn.graph.end_graph_capture()
            call_stack = ttnn.graph.extract_calltrace(trace)
            if metric["run"] == True:
                print(call_stack)
                expected_to_host_count = 0
                if result_after is None:
                    expected_to_host_count = 0
                elif isinstance(result_after, torch.Tensor):
                    expected_to_host_count = 1
                elif isinstance(result_after, (list, dict)):
                    expected_to_host_count = len(result_after)
                else:
                    print(f"Unexpected result_after type: {type(result_after)}")

                to_host_count = sum(["Tensor::cpu" in str(node) for node in call_stack])
                fallbacks_to_host_count = to_host_count - expected_to_host_count
                print(f"expected_to_host_count: {expected_to_host_count}")
                print(f"to_host_count: {to_host_count}")
                print(f"fallbacks_to_host_count: {fallbacks_to_host_count}")
                metric["ttnn_fallbacks_to_host_count"] = fallbacks_to_host_count

    if metric["run"] == True:
        try:
            # Check inference result
            metric["accuracy"] = calculate_accuracy(result_before, result_after)
        except Exception as e:
            print(f"Failed to check inference result. Raised exception: {e}")

        try:
            # Check the graph has be rewritten and contain ttnn ops
            nodes = list(option._out_fx_graphs[0].nodes)
            if not any(["aten." in str(node.target) for node in nodes]):
                metric["convert_to_ttnn"] = True
            else:
                metric["convert_to_ttnn"] = False
        except Exception as e:
            print(f"Failed to check the graph has ttnn op. Raised exception: {e}")

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] >= 0.99
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
