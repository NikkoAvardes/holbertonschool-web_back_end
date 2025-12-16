export default function hasValuesFromArray(array, set) {
  const b_array = new Set(array)
  return new Set(set).isSubsetOf(b_array)
}