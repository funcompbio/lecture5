## Numeric vectors (1-d arrays) with numpy

* An important distinction between numpy arrays and built-in lists is that
subsetting in numpy arrays creates _views_ from the original object:

   ```
   >>> v0s
   array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
   >>> subv0s = v0s[3:6] ## subset positions 3 to 5
   >>> subv0s
   array([0., 0., 0.])
   >>> subv0s[:] = 1 ## set values to 1 in this sub-array *view*
   >>> subv0s
   array([1., 1., 1.])
   >>> v0s ## changes have been propagated to the original array
   array([0., 0., 0., 1., 1., 1., 0., 0., 0., 0.])
   ```

---

## Numeric vectors (1-d arrays) with numpy
* To have a subset of an array that is a **copy**, and not a _view_, of the
original array, we should call the `copy()` function on the subsetted object:

   ```
   >>> v0s
   array([0., 0., 0., 1., 1., 1., 0., 0., 0., 0.])
   >>> subv0s = v0s[3:6].copy() ## subset and *copy* positions 3 to 5
   >>> subv0s
   array([1., 1., 1.])
   >>> subv0s[:] = 0 ## set values to 0 in this sub-array *copy*
   >>> subv0s
   array([0., 0., 0.])
   >>> v0s ## the original array remains intact
   array([0., 0., 0., 1., 1., 1., 0., 0., 0., 0.])
   ```

---

## Concluding remarks (numpy vectors and matrices)

* Subsetting in numpy provides _views_ of the original object, which
propagate changes from the subsetted object to the original one.

* To alter a subsetted object without changing the original one, you
need to explictily copy it first.
