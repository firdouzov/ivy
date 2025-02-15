"""
Collection of Jax activation functions, wrapped to fit Ivy syntax and signature.
"""

from typing import Optional

# global
import jax
import jax.numpy as jnp

# local
import ivy
from ivy.functional.backends.jax import JaxArray


def relu(x: JaxArray,
         out: Optional[JaxArray] = None)\
        -> JaxArray:
    ret = jnp.maximum(x, 0)
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def leaky_relu(x: JaxArray, alpha: Optional[float] = 0.2)\
        -> JaxArray:
    return jnp.where(x > 0, x, x * alpha)


gelu = jax.nn.gelu

def tanh(x: JaxArray)\
        -> JaxArray:
    return jnp.tanh


sigmoid = lambda x: 1 / (1 + jnp.exp(-x))


def softmax(x, axis=-1):
    exp_x = jnp.exp(x)
    return exp_x / jnp.sum(exp_x, axis, keepdims=True)


def softplus(x: JaxArray)\
        -> JaxArray:
    return jnp.log(jnp.exp(x) + 1)