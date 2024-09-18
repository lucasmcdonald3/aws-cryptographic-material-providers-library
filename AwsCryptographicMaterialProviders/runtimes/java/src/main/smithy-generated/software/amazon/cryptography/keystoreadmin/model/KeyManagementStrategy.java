// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.AwsKms;

/**
 * This configures which Key Management Operations will be used
 *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
 */
public class KeyManagementStrategy {

  /**
   * Key Store Items are authenicated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   */
  private final AwsKms AwsKmsReEncrypt;

  /**
   * Key Store Items are authenicated and re-wrapped via a Decrypt and then Encrypt request.
   *      This is two separate requests to Key Management, as compared to one.
   *      But the Decrypt requests will use the Decrypt KMS Client (and Grant Tokens),
   *      while the Encrypt requests will use the Encrypt KMS Client (and Grant Tokens).
   *      This option affords for different credentials to be utilized,
   *      based on the operation.
   *      When Generating new material,
   *      KMS GenerateDataKeyWithoutPlaintext will be executed against
   *      the Encrypt option.
   */
  private final AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt;

  protected KeyManagementStrategy(BuilderImpl builder) {
    this.AwsKmsReEncrypt = builder.AwsKmsReEncrypt();
    this.AwsKmsDecryptEncrypt = builder.AwsKmsDecryptEncrypt();
  }

  /**
   * @return Key Store Items are authenicated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   */
  public AwsKms AwsKmsReEncrypt() {
    return this.AwsKmsReEncrypt;
  }

  /**
   * @return Key Store Items are authenicated and re-wrapped via a Decrypt and then Encrypt request.
   *      This is two separate requests to Key Management, as compared to one.
   *      But the Decrypt requests will use the Decrypt KMS Client (and Grant Tokens),
   *      while the Encrypt requests will use the Encrypt KMS Client (and Grant Tokens).
   *      This option affords for different credentials to be utilized,
   *      based on the operation.
   *      When Generating new material,
   *      KMS GenerateDataKeyWithoutPlaintext will be executed against
   *      the Encrypt option.
   */
  public AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt() {
    return this.AwsKmsDecryptEncrypt;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param AwsKmsReEncrypt Key Store Items are authenicated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     */
    Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt);

    /**
     * @return Key Store Items are authenicated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     */
    AwsKms AwsKmsReEncrypt();

    /**
     * @param AwsKmsDecryptEncrypt Key Store Items are authenicated and re-wrapped via a Decrypt and then Encrypt request.
     *      This is two separate requests to Key Management, as compared to one.
     *      But the Decrypt requests will use the Decrypt KMS Client (and Grant Tokens),
     *      while the Encrypt requests will use the Encrypt KMS Client (and Grant Tokens).
     *      This option affords for different credentials to be utilized,
     *      based on the operation.
     *      When Generating new material,
     *      KMS GenerateDataKeyWithoutPlaintext will be executed against
     *      the Encrypt option.
     */
    Builder AwsKmsDecryptEncrypt(AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt);

    /**
     * @return Key Store Items are authenicated and re-wrapped via a Decrypt and then Encrypt request.
     *      This is two separate requests to Key Management, as compared to one.
     *      But the Decrypt requests will use the Decrypt KMS Client (and Grant Tokens),
     *      while the Encrypt requests will use the Encrypt KMS Client (and Grant Tokens).
     *      This option affords for different credentials to be utilized,
     *      based on the operation.
     *      When Generating new material,
     *      KMS GenerateDataKeyWithoutPlaintext will be executed against
     *      the Encrypt option.
     */
    AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt();

    KeyManagementStrategy build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms AwsKmsReEncrypt;

    protected AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyManagementStrategy model) {
      this.AwsKmsReEncrypt = model.AwsKmsReEncrypt();
      this.AwsKmsDecryptEncrypt = model.AwsKmsDecryptEncrypt();
    }

    public Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt) {
      this.AwsKmsReEncrypt = AwsKmsReEncrypt;
      return this;
    }

    public AwsKms AwsKmsReEncrypt() {
      return this.AwsKmsReEncrypt;
    }

    public Builder AwsKmsDecryptEncrypt(
      AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt
    ) {
      this.AwsKmsDecryptEncrypt = AwsKmsDecryptEncrypt;
      return this;
    }

    public AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt() {
      return this.AwsKmsDecryptEncrypt;
    }

    public KeyManagementStrategy build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KeyManagementStrategy` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KeyManagementStrategy(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.AwsKmsReEncrypt, this.AwsKmsDecryptEncrypt };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
