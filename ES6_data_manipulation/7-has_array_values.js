export default function hasValuesFromArray(array, set) {
  const b_array = new Set(array);
  const b_set = new Set(set);
  return b_set.isSubsetOf(b_array)
}