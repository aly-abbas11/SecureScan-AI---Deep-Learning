
import sys
import torch

sys.path.append("/kaggle/working/SecureSense")

from models.codebert_bilstm import SecureSenseModel


def test_output_shape():

    model = SecureSenseModel()

    input_ids = torch.randint(
        0,
        100,
        (2, 128)
    )

    attention_mask = torch.ones((2, 128))

    outputs = model(
        input_ids=input_ids,
        attention_mask=attention_mask
    )

    assert outputs.shape == (2, 2)


test_output_shape()

print("Unit test passed successfully")
